"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAccountSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id


class DescribeAccountSettingsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the settings that you want to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccountSettingsRequest:
    out: DescribeAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
