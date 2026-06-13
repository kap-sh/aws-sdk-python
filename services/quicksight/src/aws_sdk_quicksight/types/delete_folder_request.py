"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteFolderRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.restrictive_resource_id


class DeleteFolderRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the folder.</p>"""
    folder_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFolderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFolderRequest:
    out: DeleteFolderRequest = {}  # type: ignore[typeddict-item]
    return out
