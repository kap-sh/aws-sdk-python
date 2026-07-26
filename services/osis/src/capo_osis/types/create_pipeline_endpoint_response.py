"""Generated from Smithy shape ``com.amazonaws.osis#CreatePipelineEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_arn
    import capo_osis.types.pipeline_endpoint_id
    import capo_osis.types.pipeline_endpoint_status
    import capo_osis.types.string


class CreatePipelineEndpointResponse(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_osis.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline associated with the endpoint.</p>"""
    endpoint_id: NotRequired["capo_osis.types.pipeline_endpoint_id.PipelineEndpointId"]
    """<p>The unique identifier of the pipeline endpoint.</p>"""
    status: NotRequired[
        "capo_osis.types.pipeline_endpoint_status.PipelineEndpointStatus"
    ]
    """<p>The current status of the pipeline endpoint.</p>"""
    vpc_id: NotRequired["capo_osis.types.string.String"]
    """<p>The ID of the VPC where the pipeline endpoint was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipelineEndpointResponse) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "status" in value:
        import capo_osis.types.pipeline_endpoint_status

        out["Status"] = capo_osis.types.pipeline_endpoint_status.serialize_json(
            value["status"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> CreatePipelineEndpointResponse:
    out: CreatePipelineEndpointResponse = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "Status" in data:
        import capo_osis.types.pipeline_endpoint_status

        out["status"] = capo_osis.types.pipeline_endpoint_status.deserialize_json(
            data["Status"]
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
