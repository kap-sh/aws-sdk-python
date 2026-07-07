"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterAssociatedRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbClusterAssociatedRole(TypedDict, closed=True):
    role_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the IAM role.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the association between the IAM role and the DB cluster. Valid values are as follows:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>INVALID</code> </p> </li> <li> <p> <code>PENDING</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterAssociatedRole) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbClusterAssociatedRole:
    out: AwsRdsDbClusterAssociatedRole = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
