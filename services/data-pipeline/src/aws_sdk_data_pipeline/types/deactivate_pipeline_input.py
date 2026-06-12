"""Generated from Smithy shape ``com.amazonaws.datapipeline#DeactivatePipelineInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.cancel_active
    import aws_sdk_data_pipeline.types.id


class DeactivatePipelineInput(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    cancel_active: NotRequired["aws_sdk_data_pipeline.types.cancel_active.cancelActive"]
    """<p>Indicates whether to cancel any running objects. The default is true, which sets the state of any running objects to <code>CANCELED</code>. If this value is false, the pipeline is deactivated after all running objects finish.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeactivatePipelineInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    if "cancel_active" in value:
        out["cancelActive"] = value["cancel_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeactivatePipelineInput:
    out: DeactivatePipelineInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("DeactivatePipelineInput.pipeline_id required")
    if "cancelActive" in data:
        out["cancel_active"] = data["cancelActive"]
    return out
