"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.aws_account
    import capo_opensearch.types.domain_arn
    import capo_opensearch.types.endpoint
    import capo_opensearch.types.vpc_derived_info
    import capo_opensearch.types.vpc_endpoint_id
    import capo_opensearch.types.vpc_endpoint_status


class VpcEndpoint(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired["capo_opensearch.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The unique identifier of the endpoint.</p>"""
    vpc_endpoint_owner: NotRequired["capo_opensearch.types.aws_account.AWSAccount"]
    """<p>The creator of the endpoint.</p>"""
    domain_arn: NotRequired["capo_opensearch.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the domain associated with the endpoint.</p>"""
    vpc_options: NotRequired["capo_opensearch.types.vpc_derived_info.VPCDerivedInfo"]
    """<p>Options to specify the subnets and security groups for an Amazon OpenSearch Service VPC endpoint.</p>"""
    status: NotRequired["capo_opensearch.types.vpc_endpoint_status.VpcEndpointStatus"]
    """<p>The current status of the endpoint.</p>"""
    endpoint: NotRequired["capo_opensearch.types.endpoint.Endpoint"]
    """<p>The connection endpoint ID for connecting to the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpoint) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_endpoint_owner" in value:
        out["VpcEndpointOwner"] = value["vpc_endpoint_owner"]
    if "domain_arn" in value:
        out["DomainArn"] = value["domain_arn"]
    if "vpc_options" in value:
        import capo_opensearch.types.vpc_derived_info

        out["VpcOptions"] = capo_opensearch.types.vpc_derived_info.serialize_json(
            value["vpc_options"]
        )
    if "status" in value:
        import capo_opensearch.types.vpc_endpoint_status

        out["Status"] = capo_opensearch.types.vpc_endpoint_status.serialize_json(
            value["status"]
        )
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> VpcEndpoint:
    out: VpcEndpoint = {}  # type: ignore[typeddict-item]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if "VpcEndpointOwner" in data:
        out["vpc_endpoint_owner"] = data["VpcEndpointOwner"]
    if "DomainArn" in data:
        out["domain_arn"] = data["DomainArn"]
    if "VpcOptions" in data:
        import capo_opensearch.types.vpc_derived_info

        out["vpc_options"] = capo_opensearch.types.vpc_derived_info.deserialize_json(
            data["VpcOptions"]
        )
    if "Status" in data:
        import capo_opensearch.types.vpc_endpoint_status

        out["status"] = capo_opensearch.types.vpc_endpoint_status.deserialize_json(
            data["Status"]
        )
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    return out
