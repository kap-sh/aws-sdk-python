"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteDataSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_id


class DeleteDataSetRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID for the dataset that you want to delete. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataSetRequest:
    out: DeleteDataSetRequest = {}  # type: ignore[typeddict-item]
    return out
