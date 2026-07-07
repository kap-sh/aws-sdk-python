"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VpcEndpointDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.security_group_ids
    import aws_sdk_opensearchserverless.types.subnet_ids
    import aws_sdk_opensearchserverless.types.vpc_endpoint_id
    import aws_sdk_opensearchserverless.types.vpc_endpoint_name
    import aws_sdk_opensearchserverless.types.vpc_endpoint_status
    import aws_sdk_opensearchserverless.types.vpc_id


class VpcEndpointDetail(TypedDict, closed=True):
    id: NotRequired["aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The unique identifier of the endpoint.</p>"""
    name: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName"
    ]
    """<p>The name of the endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_opensearchserverless.types.vpc_id.VpcId"]
    """<p>The ID of the VPC from which you access OpenSearch Serverless.</p>"""
    subnet_ids: NotRequired["aws_sdk_opensearchserverless.types.subnet_ids.SubnetIds"]
    """<p>The ID of the subnets from which you access OpenSearch Serverless.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_opensearchserverless.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_status.VpcEndpointStatus"
    ]
    """<p>The current status of the endpoint.</p>"""
    created_date: NotRequired["int"]
    """<p>The date the endpoint was created.</p>"""
    failure_code: NotRequired["str"]
    """<p>A failure code associated with the request.</p>"""
    failure_message: NotRequired["str"]
    """<p>A message associated with the failure code.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
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
    if "status" in value:
        out["status"] = value["status"]
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpointDetail:
    out: VpcEndpointDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
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
    if "status" in data:
        out["status"] = data["status"]
    if "createdDate" in data:
        out["created_date"] = data["createdDate"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
