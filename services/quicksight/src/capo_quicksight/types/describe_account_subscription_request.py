"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAccountSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id


class DescribeAccountSubscriptionRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID associated with your Quick Sight account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAccountSubscriptionRequest:
    out: DescribeAccountSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
