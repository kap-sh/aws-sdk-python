"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeQPersonalizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id


class DescribeQPersonalizationConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the personalization configuration that the user wants described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQPersonalizationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeQPersonalizationConfigurationRequest:
    out: DescribeQPersonalizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
