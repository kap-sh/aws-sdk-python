"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbInstanceAssociatedRole``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbInstanceAssociatedRole(TypedDict):
    role_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the IAM role that is associated with the DB instance.</p>"""
    feature_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the feature associated with the IAM role.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Describes the state of the association between the IAM role and the DB instance. The <code>Status</code> property returns one of the following values:</p> <ul> <li> <p> <code>ACTIVE</code> - The IAM role ARN is associated with the DB instance and can be used to access other Amazon Web Services services on your behalf.</p> </li> <li> <p> <code>PENDING</code> - The IAM role ARN is being associated with the DB instance.</p> </li> <li> <p> <code>INVALID</code> - The IAM role ARN is associated with the DB instance. But the DB instance is unable to assume the IAM role in order to access other Amazon Web Services services on your behalf. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbInstanceAssociatedRole) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "feature_name" in value:
        out["FeatureName"] = value["feature_name"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbInstanceAssociatedRole:
    out: AwsRdsDbInstanceAssociatedRole = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "FeatureName" in data:
        out["feature_name"] = data["FeatureName"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
