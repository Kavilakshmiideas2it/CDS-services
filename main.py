from flask_cors import CORS, cross_origin
from flask import Flask, request

app = Flask(__name__)
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'

@app.route('/cds-services')
@cross_origin()
def cds_services():
    return {
        "services": [{
            "hook": "patient-view",
            "name": "CME-ster",
            "description": "hshv",
            "id": "cme-ster",
            "prefetch": {
                "patient": "Patient/{{context.patientId}}",
                "condition": "Condition?patient={{context.patientId}}",
                "observation": "Observation?patient={{context.patientId}}"
            }
        }

        ]
    }


@app.route('/cds-services/cme-ster', methods=['POST'])
@cross_origin()
def patient_view():
    hook_data = request.get_json()
    print(hook_data)
    return {
        "cards": [
            {
                "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a60",
                "summary": f"Now seeing: Test CDS for Patient - {' '.join(hook_data['prefetch']['patient']['name'][0]['given'])}",
                "source": {
                    "label": "TEST CDS SERVICES"
                },
                "indicator": "warning",
                "detail": "Patient has a history of test",
                "suggestions": [
                    {
                        "label": "test suggestion",
                        'uuid': "3333eabe-e5a6-4942-8b01-eadf3f660a6f",
                        "actions": [
                            {
                                'type': 'delete',
                                "description": "Test",
                                "resource": {
                                    "resourceType": "MedicationRequest"
                                }
                            }]

                    }
                ]
            },
            {
                "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a61",
                "summary": "Now seeing: Test CDS",
                "source": {
                    "label": "TEST CDS SERVICES"
                },
                "indicator": "critical",
                "detail": "Patient has a history of test",
                "links": [
                    {
                        "label": "test link",
                        'url': "https://ideas2it.com",
                        "type": 'absolute'
                    },
                    {
                        "label": "test link2",
                        'url': "https://example.com/launch",
                        "type": 'smart'
                    }

                ]
            }
        ]
    }


@app.route('/cds-services/cme-ster/feedback', methods=['POST'])
@cross_origin()
def feedback():
    return {"feedback": [{
            "card": "123456",
            "outcome": "overridden",
            "outcomeTimestamp": "2022-05-19T19:44:04Z",
            "overrideReasons": {
                "reason": {
                    "code": "contraindicated",
                    "display": "bad",
                    "system": "http: //example.org/cds-services/fhir/CodeSystem/override-reasons"
                },
                "userComment": "User Entered Free Text"}}]}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
