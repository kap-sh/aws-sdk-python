"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateCustomPermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.capabilities
    import aws_sdk_quicksight.types.custom_permissions_name
    import aws_sdk_quicksight.types.tag_list


class CreateCustomPermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that you want to create the custom permissions profile in.</p>"""
    custom_permissions_name: (
        "aws_sdk_quicksight.types.custom_permissions_name.CustomPermissionsName"
    )
    """<p>The name of the custom permissions profile that you want to create.</p>"""
    capabilities: NotRequired["aws_sdk_quicksight.types.capabilities.Capabilities"]
    """<p>A set of actions to include in the custom permissions profile.</p>"""
    tags: NotRequired["aws_sdk_quicksight.types.tag_list.TagList"]
    """<p>The tags to associate with the custom permissions profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomPermissionsRequest) -> dict:
    out: dict = {}
    out["CustomPermissionsName"] = value["custom_permissions_name"]
    if "capabilities" in value:
        import aws_sdk_quicksight.types.capabilities

        out["Capabilities"] = aws_sdk_quicksight.types.capabilities.serialize_json(
            value["capabilities"]
        )
    if "tags" in value:
        import aws_sdk_quicksight.types.tag_list

        out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCustomPermissionsRequest:
    out: CreateCustomPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "CustomPermissionsName" in data:
        out["custom_permissions_name"] = data["CustomPermissionsName"]
    else:
        raise DeserializationError(
            "CreateCustomPermissionsRequest.custom_permissions_name required"
        )
    if "Capabilities" in data:
        import aws_sdk_quicksight.types.capabilities

        out["capabilities"] = aws_sdk_quicksight.types.capabilities.deserialize_json(
            data["Capabilities"]
        )
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out
