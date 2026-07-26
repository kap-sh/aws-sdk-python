"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_id


class DescribeFeedbackRequest(TypedDict, closed=True):
    insight_id: NotRequired["capo_devops_guru.types.insight_id.InsightId"]
    """<p> The ID of the insight for which the feedback was provided. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFeedbackRequest) -> dict:
    out: dict = {}
    if "insight_id" in value:
        out["InsightId"] = value["insight_id"]
    return out


def deserialize_json(data: dict) -> DescribeFeedbackRequest:
    out: DescribeFeedbackRequest = {}  # type: ignore[typeddict-item]
    if "InsightId" in data:
        out["insight_id"] = data["InsightId"]
    return out
