    
    
Technical Pipeline / Project Architecture
===========================================
    

 .. raw:: html   
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                margin-top: 1em;
            }
            table, th, td {
                border: 1px solid #444;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            .expected-outcome {
                text-align: justify;
                color: #000080;
                font-style: italic;
            }
        </style>
    </head>
    <body>

        <p>The overall process for implementing the project is structured in the following pipeline:</p>

        <h2>1. Data Collection & Preprocessing</h2>
        <ul>
            <li>Extract data from existing sources such as PDF files, Excel spreadsheets, technical documents, and internal databases.</li>
            <li>Clean, structure, and normalize textual data to make it usable by AI models.</li>
            <li>Tools used may include <strong>PyMuPDF</strong>, <strong>Pandas</strong>, <strong>OpenRefine</strong>, etc.</li>
        </ul>

        <h2>2. Knowledge Base Creation</h2>
        <ul>
            <li>Organize the extracted data into a Knowledge Base.</li>
            <li>Structure the information by component, requirement, test type, and associated documentation.</li>
            <li>Possible technologies include <strong>PostgreSQL</strong>, <strong>MongoDB</strong>, and vector databases like <strong>FAISS</strong> or <strong>Weaviate</strong>.</li>
        </ul>

        <h2>3. Benchmarking & Integration of LLM / RAG Models</h2>
        <ul>
            <li>Select and experiment with different language models (LLMs) such as GPT-4, Mistral, LLaMA, etc.</li>
            <li>Integrate a <strong>Retrieval-Augmented Generation (RAG)</strong> architecture that combines knowledge base search with text generation.</li>
            <li>Evaluate performance, accuracy of responses, and domain adaptation for the automotive context.</li>
        </ul>

        <h2>4. Automatic Document Generation</h2>
        <ul>
            <li>Use generative AI models to automatically produce:
                <ul>
                    <li>Technical specifications</li>
                    <li>Test plans</li>
                    <li>Validation reports</li>
                </ul>
            </li>
            <li>Supported formats: PDF, DOCX, JSON.</li>
            <li>Integration options: <strong>LangChain</strong>, <strong>LlamaIndex</strong>, or <strong>HuggingFace Transformers</strong>.</li>
        </ul>

        <h2>5. Development of the Web Platform</h2>
        <ul>
            <li>Create a user-friendly interface allowing:
                <ul>
                    <li>Input of the component name</li>
                    <li>Submission of questions</li>
                    <li>Download of generated documents</li>
                </ul>
            </li>
            <li>Proposed technologies include: <strong>React.js</strong> or <strong>Vue.js</strong> (frontend), 
                <strong>FastAPI</strong> or <strong>Django</strong> (backend), with <strong>Docker</strong> used for deployment.
            </li>
        </ul>

        <h2>6. Key Application Features</h2>
        <table>
            <tr>
                <th>Feature</th>
                <th>Description</th>
            </tr>
            <tr>
                <td><strong>Intelligent Search</strong></td>
                <td>Find requirements based on the component name.</td>
            </tr>
            <tr>
                <td><strong>AI Q&amp;A Agent</strong></td>
                <td>Answer questions regarding the component's technical details.</td>
            </tr>
            <tr>
                <td><strong>Document Generation</strong></td>
                <td>Generate test sheets, specifications, and validation reports.</td>
            </tr>
            <tr>
                <td><strong>Requirement Explanation</strong></td>
                <td>Provide in-depth explanations of requirement functions, impacts, and associated tests.</td>
            </tr>
        </table>

    </body>
    </html>

 Expected Outcome
----------------------

.. raw:: html

         
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Technical Pipeline / Project Architecture</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                margin-top: 1em;
            }
            table, th, td {
                border: 1px solid #444;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            .expected-outcome {
                text-align: justify;
                color: #000080;
                font-style: italic;
            }
        </style>
    </head>
    <body>
  
        <p class="expected-outcome">
            An <strong>intelligent web platform</strong> that transforms a simple component name into a rich set of 
            technical information and documents. This will significantly reduce the time required for analysis, 
            documentation, and validation in the automotive domain.
        </p>

        <h2>Technologies & Tools</h2>
        <table>
            <tr>
                <th>Domain</th>
                <th>Tools / Technologies</th>
            </tr>
            <tr>
                <td><strong>Data Extraction</strong></td>
                <td>PyMuPDF, textract, Pandas</td>
            </tr>
            <tr>
                <td><strong>AI & NLP</strong></td>
                <td>OpenAI GPT, LangChain, HuggingFace</td>
            </tr>
            <tr>
                <td><strong>Vector Databases</strong></td>
                <td>FAISS, ChromaDB, Weaviate</td>
            </tr>
            <tr>
                <td><strong>Backend</strong></td>
                <td>FastAPI, Flask, Django</td>
            </tr>
            <tr>
                <td><strong>Frontend</strong></td>
                <td>React, Vue.js</td>
            </tr>
            <tr>
                <td><strong>Documentation</strong></td>
                <td>MkDocs, Sphinx, Notion</td>
            </tr>
        </table>

    </body>
    </html>
