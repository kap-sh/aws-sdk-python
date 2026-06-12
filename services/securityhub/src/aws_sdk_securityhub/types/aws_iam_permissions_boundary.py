"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamPermissionsBoundary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamPermissionsBoundary(TypedDict):
    permissions_boundary_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the policy used to set the permissions boundary.</p>"""
    permissions_boundary_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The usage type for the permissions boundary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamPermissionsBoundary) -> dict:
    out: dict = {}
    if "permissions_boundary_arn" in value:
        out["PermissionsBoundaryArn"] = value["permissions_boundary_arn"]
    if "permissions_boundary_type" in value:
        out["PermissionsBoundaryType"] = value["permissions_boundary_type"]
    return out


def deserialize_json(data: dict) -> AwsIamPermissionsBoundary:
    out: AwsIamPermissionsBoundary = {}  # type: ignore[typeddict-item]
    if "PermissionsBoundaryArn" in data:
        out["permissions_boundary_arn"] = data["PermissionsBoundaryArn"]
    if "PermissionsBoundaryType" in data:
        out["permissions_boundary_type"] = data["PermissionsBoundaryType"]
    return out
