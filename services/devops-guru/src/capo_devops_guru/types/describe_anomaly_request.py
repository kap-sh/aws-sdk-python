"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeAnomalyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.anomaly_id
    import capo_devops_guru.types.aws_account_id


class DescribeAnomalyRequest(TypedDict, closed=True):
    id: "capo_devops_guru.types.anomaly_id.AnomalyId"
    """<p> The ID of the anomaly. </p>"""
    account_id: NotRequired["capo_devops_guru.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnomalyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAnomalyRequest:
    out: DescribeAnomalyRequest = {}  # type: ignore[typeddict-item]
    return out
