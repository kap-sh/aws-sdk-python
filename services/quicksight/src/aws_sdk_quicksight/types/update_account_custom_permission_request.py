"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAccountCustomPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.custom_permissions_name


class UpdateAccountCustomPermissionRequest(TypedDict, closed=True):
    custom_permissions_name: (
        "aws_sdk_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions profile that you want to apply to an account.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account for which you want to apply a custom permissions profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountCustomPermissionRequest) -> dict:
    out: dict = {}
    out["CustomPermissionsName"] = value["custom_permissions_name"]
    return out


def deserialize_json(data: dict) -> UpdateAccountCustomPermissionRequest:
    out: UpdateAccountCustomPermissionRequest = {}  # type: ignore[typeddict-item]
    if "CustomPermissionsName" in data:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    else:
        raise DeserializationError(
            "UpdateAccountCustomPermissionRequest.custom_permissions_name required"
        )
    return out
