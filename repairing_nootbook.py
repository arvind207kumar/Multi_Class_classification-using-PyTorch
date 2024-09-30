import nbconvert
import nbformat

with open('pytorch_multiclass_classification.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Convert the notebook to Markdown
md = nbconvert.markdown.MarkdownExporter()
output, _ = md.from_notebook_node(nb)

# Save the output to a new file
with open('repaired_pytorch_multiclass_classification.md', 'w', encoding='utf-8') as f:
    f.write(output)