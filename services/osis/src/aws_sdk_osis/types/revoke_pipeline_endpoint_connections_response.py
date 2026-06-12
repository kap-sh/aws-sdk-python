"""Generated from Smithy shape ``com.amazonaws.osis#RevokePipelineEndpointConnectionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn


class RevokePipelineEndpointConnectionsResponse(TypedDict):
    pipeline_arn: NotRequired["aws_sdk_osis.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline from which endpoint connections were revoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokePipelineEndpointConnectionsResponse) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    return out


def deserialize_json(data: dict) -> RevokePipelineEndpointConnectionsResponse:
    out: RevokePipelineEndpointConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    return out
