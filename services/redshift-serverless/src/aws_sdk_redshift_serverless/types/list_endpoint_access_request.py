"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListEndpointAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.owner_account


class ListEndpointAccessRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListEndpointAccess</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>"""
    workgroup_name: NotRequired["str"]
    """<p>The name of the workgroup associated with the VPC endpoint to return.</p>"""
    vpc_id: NotRequired["str"]
    """<p>The unique identifier of the virtual private cloud with access to Amazon Redshift Serverless.</p>"""
    owner_account: NotRequired[
        "aws_sdk_redshift_serverless.types.owner_account.OwnerAccount"
    ]
    """<p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointAccessRequest) -> dict:
    out: dict = {}
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointAccessRequest:
    out: ListEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    return out
