"""Generated from Smithy shape ``com.amazonaws.pipes#SageMakerPipelineParameter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.sage_maker_pipeline_parameter_name
    import aws_sdk_pipes.types.sage_maker_pipeline_parameter_value


class SageMakerPipelineParameter(TypedDict):
    name: "aws_sdk_pipes.types.sage_maker_pipeline_parameter_name.SageMakerPipelineParameterName"
    """<p>Name of parameter to start execution of a SageMaker Model Building Pipeline.</p>"""
    value: "aws_sdk_pipes.types.sage_maker_pipeline_parameter_value.SageMakerPipelineParameterValue"
    """<p>Value of parameter to start execution of a SageMaker Model Building Pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerPipelineParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SageMakerPipelineParameter:
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
