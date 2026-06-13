"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFolderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.folder_name
    import aws_sdk_quicksight.types.restrictive_resource_id


class UpdateFolderRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the folder to update.</p>"""
    folder_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""
    name: "aws_sdk_quicksight.types.folder_name.FolderName"
    """<p>The name of the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFolderRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateFolderRequest:
    out: UpdateFolderRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateFolderRequest.name required")
    return out
