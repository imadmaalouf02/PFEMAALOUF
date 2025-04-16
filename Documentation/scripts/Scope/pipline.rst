
Technical Pipeline / Project Architecture
===========================================
.. raw:: html

     <p style="text-align: justify;"><span style="color:#000080;"><i>  
        The overall process for implementing the project is structured in the following pipeline:

    </i></span></p>
    
1. Data Collection & Preprocessing
   ----------------------------------
.. raw:: html

     <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Extract data from existing sources such as PDF files, Excel spreadsheets, technical documents, and internal databases.
   </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>  
     <li>- Clean, structure, and normalize textual data to make it usable by AI models.</li>
   
   </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Tools used may include **PyMuPDF**, **Pandas**, **OpenRefine**, etc.

    </i></span></p>
    
2. Knowledge Base Creation
   --------------------------

.. raw:: html

     <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Organize the extracted data into a Knowledge Base.
   </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Structure the information by component, requirement, test type, and associated documentation.
   </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Possible technologies include **PostgreSQL**, **MongoDB**, and vector databases like **FAISS** or **Weaviate**.
    </i></span></p>
    
3. Benchmarking & Integration of LLM / RAG Models
   -------------------------------------------------

.. raw:: html

     <p style="text-align: justify;"><span style="color:#000080;"><i>  

   - Select and experiment with different language models (LLMs) such as GPT-4, Mistral, LLaMA, etc.
   </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Integrate a <strong>Retrieval-Augmented Generation (RAG)</strong>architecture that combines knowledge base search with text generation.
   </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Evaluate performance, accuracy of responses, and domain adaptation for the automotive context.
    </i></span></p>
    
4. Automatic Document Generation
   --------------------------------


.. raw:: html

     <p style="text-align: justify;"><span style="color:#000080;"><i>  
   Use generative AI models to automatically produce:
   </i></span></p>

- Technical specifications
- Test plans
- Validation reports


.. raw:: html

     <p style="text-align: justify;"><span style="color:#000080;"><i>  

    Supported formats: PDF, DOCX, JSON.
   </i></span></p>
    <p style="text-align: justify;"><span style="color:#000080;"><i> 
    Integration options: **LangChain**, **LlamaIndex**, or **HuggingFace Transformers**.
   </i></span></p>

5. Development of the Web Platform
   ---------------------------------


.. raw:: html

     <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Create a user-friendly interface allowing:
      </i></span></p>
- Input of the component name
- Submission of questions
- Download of generated documents


.. raw:: html

     <p style="text-align: justify;"><span style="color:#000080;"><i>  
   - Proposed technologies include: **React.js** or **Vue.js** (frontend), **FastAPI** or **Django** (backend), with **Docker** used for deployment.
   </i></span></p>


6. Key Application Features
   --------------------------

.. raw:: html

   .. raw:: html

         
    
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




    <p style="text-align: justify;"><span style="color:#000080;"><i>    
    An <span style="color:#000080;">intelligent web platform</span><span style="color:#000080;"> that transforms a simple component name into a rich set of technical information and documents. This will significantly reduce the time required for analysis, documentation, and validation in the automotive domain.
    </i></span></p>


Technologies & Tools
_____________________

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
