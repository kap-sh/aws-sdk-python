"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_id


class DescribeDataSetRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID for the dataset that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDataSetRequest:
    out: DescribeDataSetRequest = {}  # type: ignore[typeddict-item]
    return out
