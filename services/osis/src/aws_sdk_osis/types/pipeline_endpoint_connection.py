"""Generated from Smithy shape ``com.amazonaws.osis#PipelineEndpointConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.aws_account_id
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.pipeline_endpoint_id
    import aws_sdk_osis.types.pipeline_endpoint_status


class PipelineEndpointConnection(TypedDict, closed=True):
    pipeline_arn: NotRequired["aws_sdk_osis.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline in the endpoint connection.</p>"""
    endpoint_id: NotRequired[
        "aws_sdk_osis.types.pipeline_endpoint_id.PipelineEndpointId"
    ]
    """<p>The unique identifier of the endpoint in the connection.</p>"""
    status: NotRequired[
        "aws_sdk_osis.types.pipeline_endpoint_status.PipelineEndpointStatus"
    ]
    """<p>The current status of the pipeline endpoint connection.</p>"""
    vpc_endpoint_owner: NotRequired["aws_sdk_osis.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account ID that owns the VPC endpoint used in this connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineEndpointConnection) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "status" in value:
        import aws_sdk_osis.types.pipeline_endpoint_status

        out["Status"] = aws_sdk_osis.types.pipeline_endpoint_status.serialize_json(
            value["status"]
        )
    if "vpc_endpoint_owner" in value:
        out["VpcEndpointOwner"] = value["vpc_endpoint_owner"]
    return out


def deserialize_json(data: dict) -> PipelineEndpointConnection:
    out: PipelineEndpointConnection = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "Status" in data:
        import aws_sdk_osis.types.pipeline_endpoint_status

        out["status"] = aws_sdk_osis.types.pipeline_endpoint_status.deserialize_json(
            data["Status"]
        )
    if "VpcEndpointOwner" in data:
        out["vpc_endpoint_owner"] = data["VpcEndpointOwner"]
    return out
