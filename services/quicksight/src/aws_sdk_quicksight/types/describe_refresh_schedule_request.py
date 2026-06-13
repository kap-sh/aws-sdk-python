"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeRefreshScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.string


class DescribeRefreshScheduleRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dataset.</p>"""
    schedule_id: "aws_sdk_quicksight.types.string.String"
    """<p>The ID of the refresh schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRefreshScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRefreshScheduleRequest:
    out: DescribeRefreshScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
