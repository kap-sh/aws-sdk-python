"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFolderRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.restrictive_resource_id


class DescribeFolderRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the folder.</p>"""
    folder_id: "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFolderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFolderRequest:
    out: DescribeFolderRequest = {}  # type: ignore[typeddict-item]
    return out
