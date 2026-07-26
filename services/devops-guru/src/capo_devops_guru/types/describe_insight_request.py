"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeInsightRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.aws_account_id
    import capo_devops_guru.types.insight_id


class DescribeInsightRequest(TypedDict, closed=True):
    id: "capo_devops_guru.types.insight_id.InsightId"
    """<p> The ID of the insight. </p>"""
    account_id: NotRequired["capo_devops_guru.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the member account in the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInsightRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInsightRequest:
    out: DescribeInsightRequest = {}  # type: ignore[typeddict-item]
    return out
