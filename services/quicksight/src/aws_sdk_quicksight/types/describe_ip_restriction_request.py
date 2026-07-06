"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeIpRestrictionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id


class DescribeIpRestrictionRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the IP rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIpRestrictionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeIpRestrictionRequest:
    out: DescribeIpRestrictionRequest = {}  # type: ignore[typeddict-item]
    return out
