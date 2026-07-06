"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterIamRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterIamRole(TypedDict, closed=True):
    apply_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the IAM role's association with the cluster.</p> <p>Valid values: <code>in-sync</code> | <code>adding</code> | <code>removing</code> </p>"""
    iam_role_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the IAM role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterIamRole) -> dict:
    out: dict = {}
    if "apply_status" in value:
        out["ApplyStatus"] = value["apply_status"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterIamRole:
    out: AwsRedshiftClusterIamRole = {}  # type: ignore[typeddict-item]
    if "ApplyStatus" in data:
        out["apply_status"] = data["ApplyStatus"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    return out
