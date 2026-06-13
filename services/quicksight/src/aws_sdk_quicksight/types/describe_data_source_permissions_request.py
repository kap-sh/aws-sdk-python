"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSourcePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.resource_id


class DescribeDataSourcePermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    data_source_id: "aws_sdk_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSourcePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDataSourcePermissionsRequest:
    out: DescribeDataSourcePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
