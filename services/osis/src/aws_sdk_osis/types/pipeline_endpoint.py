"""Generated from Smithy shape ``com.amazonaws.osis#PipelineEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.pipeline_endpoint_id
    import aws_sdk_osis.types.pipeline_endpoint_status
    import aws_sdk_osis.types.pipeline_endpoint_vpc_options
    import aws_sdk_osis.types.string


class PipelineEndpoint(TypedDict, closed=True):
    pipeline_arn: NotRequired["aws_sdk_osis.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline associated with this endpoint.</p>"""
    endpoint_id: NotRequired[
        "aws_sdk_osis.types.pipeline_endpoint_id.PipelineEndpointId"
    ]
    """<p>The unique identifier for the pipeline endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_osis.types.pipeline_endpoint_status.PipelineEndpointStatus"
    ]
    """<p>The current status of the pipeline endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The ID of the VPC where the pipeline endpoint is created.</p>"""
    vpc_options: NotRequired[
        "aws_sdk_osis.types.pipeline_endpoint_vpc_options.PipelineEndpointVpcOptions"
    ]
    """<p>Configuration options for the VPC endpoint, including subnet and security group settings.</p>"""
    ingest_endpoint_url: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The URL used to ingest data to the pipeline through the VPC endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineEndpoint) -> dict:
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
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "vpc_options" in value:
        import aws_sdk_osis.types.pipeline_endpoint_vpc_options

        out["VpcOptions"] = (
            aws_sdk_osis.types.pipeline_endpoint_vpc_options.serialize_json(
                value["vpc_options"]
            )
        )
    if "ingest_endpoint_url" in value:
        out["IngestEndpointUrl"] = value["ingest_endpoint_url"]
    return out


def deserialize_json(data: dict) -> PipelineEndpoint:
    out: PipelineEndpoint = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "Status" in data:
        import aws_sdk_osis.types.pipeline_endpoint_status

        out["status"] = aws_sdk_osis.types.pipeline_endpoint_status.deserialize_json(
            data["Status"]
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "VpcOptions" in data:
        import aws_sdk_osis.types.pipeline_endpoint_vpc_options

        out["vpc_options"] = (
            aws_sdk_osis.types.pipeline_endpoint_vpc_options.deserialize_json(
                data["VpcOptions"]
            )
        )
    if "IngestEndpointUrl" in data:
        out["ingest_endpoint_url"] = data["IngestEndpointUrl"]
    return out
