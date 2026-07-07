"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VpcEndpointSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_arn
    import aws_sdk_elasticsearch_service.types.string
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_id
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_status


class VpcEndpointSummary(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired[
        "aws_sdk_elasticsearch_service.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>The unique identifier of the endpoint.</p>"""
    vpc_endpoint_owner: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>The creator of the endpoint.</p>"""
    domain_arn: NotRequired["aws_sdk_elasticsearch_service.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the domain associated with the endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_elasticsearch_service.types.vpc_endpoint_status.VpcEndpointStatus"
    ]
    """<p>The current status of the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointSummary) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_endpoint_owner" in value:
        out["VpcEndpointOwner"] = value["vpc_endpoint_owner"]
    if "domain_arn" in value:
        out["DomainArn"] = value["domain_arn"]
    if "status" in value:
        import aws_sdk_elasticsearch_service.types.vpc_endpoint_status

        out["Status"] = (
            aws_sdk_elasticsearch_service.types.vpc_endpoint_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcEndpointSummary:
    out: VpcEndpointSummary = {}  # type: ignore[typeddict-item]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if "VpcEndpointOwner" in data:
        out["vpc_endpoint_owner"] = data["VpcEndpointOwner"]
    if "DomainArn" in data:
        out["domain_arn"] = data["DomainArn"]
    if "Status" in data:
        import aws_sdk_elasticsearch_service.types.vpc_endpoint_status

        out["status"] = (
            aws_sdk_elasticsearch_service.types.vpc_endpoint_status.deserialize_json(
                data["Status"]
            )
        )
    return out
