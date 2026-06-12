"""Generated from Smithy shape ``com.amazonaws.datapipeline#GetPipelineDefinitionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.string


class GetPipelineDefinitionInput(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    version: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>The version of the pipeline definition to retrieve. Set this parameter to <code>latest</code> (default) to use the last definition saved to the pipeline or <code>active</code> to use the last definition that was activated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineDefinitionInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineDefinitionInput:
    out: GetPipelineDefinitionInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("GetPipelineDefinitionInput.pipeline_id required")
    if "version" in data:
        out["version"] = data["version"]
    return out
