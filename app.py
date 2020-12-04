from flask import Flask, jsonify, render_template, request
import convert
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/convert', methods=["POST"])
def get_result():
    orig_text = request.form['text']
    direction = request.form['direction']

    if direction == 't2nh':
        (conv_text, highlights) = convert.convert_t2nh(orig_text)
        orig_alphabet = "Teeter"
        conv_alphabet = "Newell-Hale"
        to_mark = 'kw'
    elif direction == 'nh2t':
        (conv_text, highlights) = convert.convert_nh2t(orig_text)
        orig_alphabet = "Newell-Hale"
        conv_alphabet = "Teeter"
        to_mark = "q"
    else:
        assert False

    ranges = [{'start':h,'length':1} for h in highlights]

    orig_text = orig_text.split('\n')
    conv_text = conv_text.split('\n')

    # This isn't a great solution because it would require conv_html
    # to be passed to the template with |safe, which might not be all
    # that safe. It would be better to just implement this in
    # javascript in the template.
    # conv_html = ''
    # highlights = set(highlights)
    # for i in range(len(conv_text)):
    #     if i in highlights:
    #         conv_html += "<mark>" + conv_text[i] + "</mark>"
    #     else:
    #         conv_html += conv_text[i]
    # conv_html = conv_html.replace('\n', '<br>')
    # conv_text = conv_html

    # ***** This solution ignores the highlight ranges returned by
    # convert Any kw left converting to NH, and any q left converting
    # to T should be highlighted. This solution simply applies that
    # heuristic. This could change if highlight becomes more
    # sophisticated with knowledge of morphology, but for now it
    # works... *****

    return render_template("result.html",
                           orig_text=orig_text,
                           conv_text=conv_text,
                           orig_alphabet=orig_alphabet,
                           conv_alphabet=conv_alphabet,
                           ranges=ranges,
                           to_mark=to_mark)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()

