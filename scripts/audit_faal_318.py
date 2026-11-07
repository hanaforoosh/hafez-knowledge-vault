from pathlib import Path
import re,json
root=Path('/home/mahrad/Obsidian/Hafez')
p=root/'01-Ghazals/318.md'
t=p.read_text(encoding='utf-8')
links=re.findall(r'\[\[([^\]\n]+)\]\]',t)
missing=[]
for link in links:
    target=link.split('|')[0].split('#')[0]
    fp=root/'01-Ghazals'/f'{target}.md' if target.isdigit() else root/(target+'.md')
    if not fp.exists(): missing.append(target)
related=['97','123','348','446','471']
reciprocal={n:(root/'01-Ghazals'/f'{n}.md').read_text(encoding='utf-8').count('[[318]]') for n in related}
out={
 'utf8':'valid',
 'lines':len(t.splitlines()),
 'missing_targets':sorted(set(missing)),
 'placeholders':re.findall(r'\{(?:now|number|source|title)\}',t),
 'multiline_links':len(re.findall(r'\[\[[^\]]*\n[^\]]*\]\]',t)),
 'nested_link_marker':'[[[[' in t or ']]]]' in t,
 'reciprocal_counts':reciprocal,
 'divan_has_318':'[[318]]' in (root/'00-Index/دیوان حافظ.md').read_text(encoding='utf-8')
}
print(json.dumps(out, ensure_ascii=False, indent=2))
