"""Generated from Smithy shape ``com.amazonaws.eventbridge#SageMakerPipelineParameter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.sage_maker_pipeline_parameter_name
    import aws_sdk_eventbridge.types.sage_maker_pipeline_parameter_value


class SageMakerPipelineParameter(TypedDict):
    name: "aws_sdk_eventbridge.types.sage_maker_pipeline_parameter_name.SageMakerPipelineParameterName"
    """<p>Name of parameter to start execution of a SageMaker AI Model Building Pipeline.</p>"""
    value: "aws_sdk_eventbridge.types.sage_maker_pipeline_parameter_value.SageMakerPipelineParameterValue"
    """<p>Value of parameter to start execution of a SageMaker AI Model Building Pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SageMakerPipelineParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SageMakerPipelineParameter:
    out: SageMakerPipelineParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SageMakerPipelineParameter.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("SageMakerPipelineParameter.value required")
    return out
