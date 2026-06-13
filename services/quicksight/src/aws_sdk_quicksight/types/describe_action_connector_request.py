"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeActionConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class DescribeActionConnectorRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that contains the action connector.</p>"""
    action_connector_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of the action connector to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActionConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeActionConnectorRequest:
    out: DescribeActionConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
