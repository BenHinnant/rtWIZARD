from flask import Flask, jsonify, render_template, request, send_from_directory, send_file
from io import BytesIO
from . import custom_labware_generator

app = Flask(__name__)

# global variable: sets the type of test cassette the labware generator will use
test_type = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tests', strict_slashes=False)
def test_index():
    return render_template('tests/index.html')

@app.route('/tests/bioline_dengue', strict_slashes=False)
def bioline_dengue():
    global test_type
    test_type = 'bioline_dengue_igg_igm'
    return render_template('tests/bioline_dengue.html')

@app.route('/tests/dengucheck', strict_slashes=False)
def denguecheck():
    global test_type
    test_type = 'dengucheck-wb'
    return render_template('tests/dengucheck.html')

@app.route('/tests/dengue_duo', strict_slashes=False)
def dengue_duo():
    global test_type
    test_type = 'dengue_duo_cassette'
    return render_template('tests/dengue_duo.html')

@app.route('/tests/onsite_dengue', strict_slashes=False)
def onsite_dengue():
    global test_type
    test_type = 'onsite_dengue_igg_rapid_test'
    return render_template('tests/onsite_dengue.html')

@app.route('/tests/gdx70-2', strict_slashes=False)
def gdx70_2():
    global test_type
    test_type = 'gdx70-2_herdscreen_asf_antibody'
    return render_template('tests/gdx70-2.html')

@app.route('/tests/ingezim_asf_crom', strict_slashes=False)
def ingezim_asf_crom():
    global test_type
    test_type = 'ingezim_asf_crom_ag'
    return render_template('tests/ingezim_asf_crom.html')

@app.route('/tests/ingezim_asfv_csfv', strict_slashes=False)
def ingezim_asfv_csfv():
    global test_type
    test_type = 'ingezim_asfv_csfv_crom_ab'
    return render_template('tests/ingezim_asfv_csfv.html')

@app.route('/tests/ingezim_ppa_crom', strict_slashes=False)
def ingezim_ppa_crom():
    global test_type
    test_type = 'ingezim_ppa_crom'
    return render_template('tests/ingezim_ppa_crom.html')

@app.route('/tests/rapid_asfv_ag', strict_slashes=False)
def rapid_asfv_ag():
    global test_type
    test_type = 'rapid_asfv_ag'
    return render_template('tests/rapid_asfv_ag.html')

@app.route('/tests/one_well', strict_slashes=False)
def one_well():
    global test_type
    test_type = 'one_well_rapid_test'
    return render_template('tests/one_well.html')

@app.route('/tests/two_well', strict_slashes=False)
def two_well():
    global test_type
    test_type = 'two_well_rapid_test'
    return render_template('tests/two_well.html')

@app.route('/tests/labware_generator', strict_slashes=False, methods=['POST'])
def labware_form_processor():
    # handle the POST request
    if request.method == 'POST':

        # get the form data and VALIDATE it before processing
        try:
            num_wells = int(request.form.get('num_wells').strip())
            distA = float(request.form.get('distA').strip())
            distB = float(request.form.get('distB').strip())
            distC = float(request.form.get('distC').strip())
            distD = float(request.form.get('distD').strip())

            # only allow 1 or 2 wells
            if num_wells not in [1,2]:
                raise ValueError

        except ValueError:
            return '''<h1>Invalid input</h1>'''

        # return a zip file to the user containing the labware
        return send_file(
            path_or_file=custom_labware_generator.generate_labware_zip_file(test_type, num_wells, distA, distB, distC, distD),
            mimetype='application/zip',
            download_name='custom_labware.zip',
            as_attachment=True
        )


if __name__ == '__main__':
    app.run(debug=True)
