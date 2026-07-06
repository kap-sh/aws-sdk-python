"""Generated from Smithy shape ``com.amazonaws.datapipeline#CreatePipelineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id


class CreatePipelineOutput(TypedDict, closed=True):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID that AWS Data Pipeline assigns the newly created pipeline. For example, <code>df-06372391ZG65EXAMPLE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePipelineOutput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePipelineOutput:
    out: CreatePipelineOutput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("CreatePipelineOutput.pipeline_id required")
    return out
