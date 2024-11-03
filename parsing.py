import unstructured

def extract_metadata(file_content):
    doc = unstructured.Document(file_content)
    metadata = doc.extract_metadata()
    return metadata
