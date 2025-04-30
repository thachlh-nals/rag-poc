flowchart TD
    A[Detect Change in Google Spreadsheet] -->|Trigger: onEdit/onChange| B[Convert Google Spreadsheet to PDF]
    B -->|Export sheet/workbook to PDF| C[Save PDF to Google Drive]
    C --> D[Prepare for Upload]
    D -->|Read PDF (binary data or download)| E[Upload PDF to Qdrant]
    E -->|Convert PDF to vector embedding (if needed)| F[Generate Embedding using OpenAI/Cohere/Huggingface]
    F -->|Upload embedding with metadata| G[Store in Qdrant]