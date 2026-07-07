"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSetRefreshPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_id


class DescribeDataSetRefreshPropertiesRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_set_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSetRefreshPropertiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDataSetRefreshPropertiesRequest:
    out: DescribeDataSetRefreshPropertiesRequest = {}  # type: ignore[typeddict-item]
    return out
