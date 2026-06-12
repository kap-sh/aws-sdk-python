"""Generated from Smithy shape ``com.amazonaws.frauddetector#EvaluatedExternalModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.boolean
    import aws_sdk_frauddetector.types.map_of_strings
    import aws_sdk_frauddetector.types.string


class EvaluatedExternalModel(TypedDict):
    model_endpoint: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p> The endpoint of the external (Amazon Sagemaker) model. </p>"""
    use_event_variables: NotRequired["aws_sdk_frauddetector.types.boolean.Boolean"]
    """<p> Indicates whether event variables were used to generate predictions. </p>"""
    input_variables: NotRequired[
        "aws_sdk_frauddetector.types.map_of_strings.MapOfStrings"
    ]
    """<p> Input variables use for generating predictions. </p>"""
    output_variables: NotRequired[
        "aws_sdk_frauddetector.types.map_of_strings.MapOfStrings"
    ]
    """<p> Output variables. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatedExternalModel) -> dict:
    out: dict = {}
    if "model_endpoint" in value:
        out["modelEndpoint"] = value["model_endpoint"]
    if "use_event_variables" in value:
        out["useEventVariables"] = value["use_event_variables"]
    if "input_variables" in value:
        import aws_sdk_frauddetector.types.map_of_strings

        out["inputVariables"] = (
            aws_sdk_frauddetector.types.map_of_strings.serialize_aws_json_1_1(
                value["input_variables"]
            )
        )
    if "output_variables" in value:
        import aws_sdk_frauddetector.types.map_of_strings

        out["outputVariables"] = (
            aws_sdk_frauddetector.types.map_of_strings.serialize_aws_json_1_1(
                value["output_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatedExternalModel:
    out: EvaluatedExternalModel = {}  # type: ignore[typeddict-item]
    if "modelEndpoint" in data:
        out["model_endpoint"] = data["modelEndpoint"]
    if "useEventVariables" in data:
        out["use_event_variables"] = data["useEventVariables"]
    if "inputVariables" in data:
        import aws_sdk_frauddetector.types.map_of_strings

        out["input_variables"] = (
            aws_sdk_frauddetector.types.map_of_strings.deserialize_aws_json_1_1(
                data["inputVariables"]
            )
        )
    if "outputVariables" in data:
        import aws_sdk_frauddetector.types.map_of_strings

        out["output_variables"] = (
            aws_sdk_frauddetector.types.map_of_strings.deserialize_aws_json_1_1(
                data["outputVariables"]
            )
        )
    return out
