"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.security_group_ids
    import capo_opensearchserverless.types.subnet_ids
    import capo_opensearchserverless.types.vpc_endpoint_name
    import capo_opensearchserverless.types.vpc_id


class CreateVpcEndpointRequest(TypedDict, closed=True):
    name: "capo_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName"
    """<p>The name of the interface endpoint.</p>"""
    vpc_id: "capo_opensearchserverless.types.vpc_id.VpcId"
    """<p>The ID of the VPC from which you'll access OpenSearch Serverless.</p>"""
    subnet_ids: "capo_opensearchserverless.types.subnet_ids.SubnetIds"
    """<p>The ID of one or more subnets from which you'll access OpenSearch Serverless.</p>"""
    security_group_ids: NotRequired[
        "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVpcEndpointRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["vpcId"] = value["vpc_id"]
    import capo_opensearchserverless.types.subnet_ids

    out["subnetIds"] = (
        capo_opensearchserverless.types.subnet_ids.serialize_aws_json_1_0(
            value["subnet_ids"]
        )
    )
    if "security_group_ids" in value:
        import capo_opensearchserverless.types.security_group_ids

        out["securityGroupIds"] = (
            capo_opensearchserverless.types.security_group_ids.serialize_aws_json_1_0(
                value["security_group_ids"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVpcEndpointRequest:
    out: CreateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateVpcEndpointRequest.name required")
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("CreateVpcEndpointRequest.vpc_id required")
    if "subnetIds" in data:
        import capo_opensearchserverless.types.subnet_ids

        out["subnet_ids"] = (
            capo_opensearchserverless.types.subnet_ids.deserialize_aws_json_1_0(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("CreateVpcEndpointRequest.subnet_ids required")
    if "securityGroupIds" in data:
        import capo_opensearchserverless.types.security_group_ids

        out["security_group_ids"] = (
            capo_opensearchserverless.types.security_group_ids.deserialize_aws_json_1_0(
                data["securityGroupIds"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
