from InstructorEmbedding import INSTRUCTOR
xl = INSTRUCTOR('hkunlp/instructor-xl')
large = INSTRUCTOR('hkunlp/instructor-large')

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/embed', methods=['POST'])
def embed():
    if request.method == 'POST':
        data = request.json  # Assuming the data is sent as JSON in the request body

        text = data.get('text')
        model = data.get('model')

        if model = "instructor-xl":
            embeddings = xl.encode(data.get('text')).tolist()
        else:
            embeddings = large.encode(data.get('text')).tolist()
            
        # Process the data and generate a response
        response_data = {
            "text": text,
            "embeddings": embeddings
        }

        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)