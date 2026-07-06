"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateVpcEndpointDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.security_group_ids
    import aws_sdk_opensearchserverless.types.subnet_ids
    import aws_sdk_opensearchserverless.types.vpc_endpoint_id
    import aws_sdk_opensearchserverless.types.vpc_endpoint_name
    import aws_sdk_opensearchserverless.types.vpc_endpoint_status


class UpdateVpcEndpointDetail(TypedDict, closed=True):
    id: NotRequired["aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The unique identifier of the endpoint.</p>"""
    name: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName"
    ]
    """<p>The name of the endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_status.VpcEndpointStatus"
    ]
    """<p>The current status of the endpoint update process.</p>"""
    subnet_ids: NotRequired["aws_sdk_opensearchserverless.types.subnet_ids.SubnetIds"]
    """<p>The ID of the subnets from which you access OpenSearch Serverless.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_opensearchserverless.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The timestamp of when the endpoint was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVpcEndpointDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "subnet_ids" in value:
        import aws_sdk_opensearchserverless.types.subnet_ids

        out["subnetIds"] = (
            aws_sdk_opensearchserverless.types.subnet_ids.serialize_aws_json_1_0(
                value["subnet_ids"]
            )
        )
    if "security_group_ids" in value:
        import aws_sdk_opensearchserverless.types.security_group_ids

        out["securityGroupIds"] = (
            aws_sdk_opensearchserverless.types.security_group_ids.serialize_aws_json_1_0(
                value["security_group_ids"]
            )
        )
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVpcEndpointDetail:
    out: UpdateVpcEndpointDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "subnetIds" in data:
        import aws_sdk_opensearchserverless.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_opensearchserverless.types.subnet_ids.deserialize_aws_json_1_0(
                data["subnetIds"]
            )
        )
    if "securityGroupIds" in data:
        import aws_sdk_opensearchserverless.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_opensearchserverless.types.security_group_ids.deserialize_aws_json_1_0(
                data["securityGroupIds"]
            )
        )
    if "lastModifiedDate" in data:
        out["last_modified_date"] = data["lastModifiedDate"]
    return out
