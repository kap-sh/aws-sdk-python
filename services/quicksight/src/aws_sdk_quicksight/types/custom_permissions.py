"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPermissions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.capabilities
    import aws_sdk_quicksight.types.custom_permissions_name


class CustomPermissions(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the custom permissions profile.</p>"""
    custom_permissions_name: NotRequired[
        "aws_sdk_quicksight.types.custom_permissions_name.CustomPermissionsName"
    ]
    """<p>The name of the custom permissions profile.</p>"""
    capabilities: NotRequired["aws_sdk_quicksight.types.capabilities.Capabilities"]
    """<p>A set of actions in the custom permissions profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPermissions) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "custom_permissions_name" in value:
        out["CustomPermissionsName"] = value["custom_permissions_name"]
    if "capabilities" in value:
        import aws_sdk_quicksight.types.capabilities

        out["Capabilities"] = aws_sdk_quicksight.types.capabilities.serialize_json(
            value["capabilities"]
        )
    return out


def deserialize_json(data: dict) -> CustomPermissions:
    out: CustomPermissions = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CustomPermissionsName" in data:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    if "Capabilities" in data:
        import aws_sdk_quicksight.types.capabilities

        out["capabilities"] = aws_sdk_quicksight.types.capabilities.deserialize_json(
            data["Capabilities"]
        )
    return out
