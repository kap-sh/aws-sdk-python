"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteRefreshScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.string


class DeleteRefreshScheduleRequest(TypedDict, closed=True):
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dataset.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    schedule_id: "aws_sdk_quicksight.types.string.String"
    """<p>The ID of the refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRefreshScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRefreshScheduleRequest:
    out: DeleteRefreshScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
