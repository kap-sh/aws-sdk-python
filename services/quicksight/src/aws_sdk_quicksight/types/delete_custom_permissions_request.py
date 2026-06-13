"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteCustomPermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.custom_permissions_name


class DeleteCustomPermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the custom permissions profile that you want to delete.</p>"""
    custom_permissions_name: (
        "aws_sdk_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions profile that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomPermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomPermissionsRequest:
    out: DeleteCustomPermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
