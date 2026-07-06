"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterSecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterClusterSecurityGroup(TypedDict, closed=True):
    cluster_security_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the cluster security group.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the cluster security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterSecurityGroup) -> dict:
    out: dict = {}
    if "cluster_security_group_name" in value:
        out["ClusterSecurityGroupName"] = value["cluster_security_group_name"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterClusterSecurityGroup:
    out: AwsRedshiftClusterClusterSecurityGroup = {}  # type: ignore[typeddict-item]
    if "ClusterSecurityGroupName" in data:
        out["cluster_security_group_name"] = data["ClusterSecurityGroupName"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
