"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetPipelineStateInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_name


class GetPipelineStateInput(TypedDict):
    name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline about which you want to get information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineStateInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineStateInput:
    out: GetPipelineStateInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPipelineStateInput.name required")
    return out
