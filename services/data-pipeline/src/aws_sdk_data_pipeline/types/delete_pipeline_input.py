"""Generated from Smithy shape ``com.amazonaws.datapipeline#DeletePipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id


class DeletePipelineInput(TypedDict, closed=True):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePipelineInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePipelineInput:
    out: DeletePipelineInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("DeletePipelineInput.pipeline_id required")
    return out
