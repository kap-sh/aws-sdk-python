"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.model_input_data_format
    import capo_frauddetector.types.model_input_template
    import capo_frauddetector.types.use_event_variables


class ModelInputConfiguration(TypedDict, closed=True):
    event_type_name: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The event type name.</p>"""
    format: NotRequired[
        "capo_frauddetector.types.model_input_data_format.ModelInputDataFormat"
    ]
    """<p> The format of the model input configuration. The format differs depending on if it is passed through to SageMaker or constructed by Amazon Fraud Detector.</p>"""
    use_event_variables: (
        "capo_frauddetector.types.use_event_variables.UseEventVariables"
    )
    """<p>The event variables.</p>"""
    json_input_template: NotRequired[
        "capo_frauddetector.types.model_input_template.modelInputTemplate"
    ]
    """<p> Template for constructing the JSON input-data sent to SageMaker. At event-evaluation, the placeholders for variable names in the template will be replaced with the variable values before being sent to SageMaker. </p>"""
    csv_input_template: NotRequired[
        "capo_frauddetector.types.model_input_template.modelInputTemplate"
    ]
    """<p> Template for constructing the CSV input-data sent to SageMaker. At event-evaluation, the placeholders for variable-names in the template will be replaced with the variable values before being sent to SageMaker. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelInputConfiguration) -> dict:
    out: dict = {}
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "format" in value:
        import capo_frauddetector.types.model_input_data_format

        out["format"] = (
            capo_frauddetector.types.model_input_data_format.serialize_aws_json_1_1(
                value["format"]
            )
        )
    out["useEventVariables"] = value["use_event_variables"]
    if "json_input_template" in value:
        out["jsonInputTemplate"] = value["json_input_template"]
    if "csv_input_template" in value:
        out["csvInputTemplate"] = value["csv_input_template"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelInputConfiguration:
    out: ModelInputConfiguration = {}  # type: ignore[typeddict-item]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "format" in data:
        import capo_frauddetector.types.model_input_data_format

        out["format"] = (
            capo_frauddetector.types.model_input_data_format.deserialize_aws_json_1_1(
                data["format"]
            )
        )
    if "useEventVariables" in data:
        out["use_event_variables"] = data["useEventVariables"]
    else:
        raise DeserializationError(
            "ModelInputConfiguration.use_event_variables required"
        )
    if "jsonInputTemplate" in data:
        out["json_input_template"] = data["jsonInputTemplate"]
    if "csvInputTemplate" in data:
        out["csv_input_template"] = data["csvInputTemplate"]
    return out
