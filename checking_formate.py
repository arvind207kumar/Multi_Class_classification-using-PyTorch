import nbformat

try:
    with open('pytorch_multiclass_classification.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    with open('repaired_notebook.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print("Notebook repaired successfully!")
except Exception as e:
    print(f"Error repairing notebook: {e}")