"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateCustomPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.capabilities
    import aws_sdk_quicksight.types.custom_permissions_name


class UpdateCustomPermissionsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the custom permissions profile that you want to update.</p>"""
    custom_permissions_name: (
        "aws_sdk_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions profile that you want to update.</p>"""
    capabilities: NotRequired["aws_sdk_quicksight.types.capabilities.Capabilities"]
    """<p>A set of actions to include in the custom permissions profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomPermissionsRequest) -> dict:
    out: dict = {}
    if "capabilities" in value:
        import aws_sdk_quicksight.types.capabilities

        out["Capabilities"] = aws_sdk_quicksight.types.capabilities.serialize_json(
            value["capabilities"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCustomPermissionsRequest:
    out: UpdateCustomPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "Capabilities" in data:
        import aws_sdk_quicksight.types.capabilities

        out["capabilities"] = aws_sdk_quicksight.types.capabilities.deserialize_json(
            data["Capabilities"]
        )
    return out
