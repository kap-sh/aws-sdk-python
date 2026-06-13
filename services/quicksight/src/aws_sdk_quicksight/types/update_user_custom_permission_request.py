"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateUserCustomPermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.custom_permissions_name
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.user_name


class UpdateUserCustomPermissionRequest(TypedDict):
    user_name: "aws_sdk_quicksight.types.user_name.UserName"
    """<p>The username of the user that you want to update custom permissions for.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the custom permission configuration that you want to update.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that the user belongs to.</p>"""
    custom_permissions_name: (
        "aws_sdk_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserCustomPermissionRequest) -> dict:
    out: dict = {}
    out["CustomPermissionsName"] = value["custom_permissions_name"]
    return out


def deserialize_json(data: dict) -> UpdateUserCustomPermissionRequest:
    out: UpdateUserCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    if "CustomPermissionsName" in data:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    else:
        raise DeserializationError(
            "UpdateUserCustomPermissionRequest.custom_permissions_name required"
        )
    return out
