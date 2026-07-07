"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDmsReplicationInstanceVpcSecurityGroupsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsDmsReplicationInstanceVpcSecurityGroupsDetails(TypedDict, closed=True):
    vpc_security_group_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The identifier of the VPC security group that’s associated with the replication instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDmsReplicationInstanceVpcSecurityGroupsDetails) -> dict:
    out: dict = {}
    if "vpc_security_group_id" in value:
        out["VpcSecurityGroupId"] = value["vpc_security_group_id"]
    return out


def deserialize_json(data: dict) -> AwsDmsReplicationInstanceVpcSecurityGroupsDetails:
    out: AwsDmsReplicationInstanceVpcSecurityGroupsDetails = {}  # type: ignore[typeddict-item]
    if "VpcSecurityGroupId" in data:
        out["vpc_security_group_id"] = data["VpcSecurityGroupId"]
    return out
