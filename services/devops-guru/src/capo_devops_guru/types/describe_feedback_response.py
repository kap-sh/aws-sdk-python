"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeFeedbackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_feedback


class DescribeFeedbackResponse(TypedDict, closed=True):
    insight_feedback: NotRequired[
        "capo_devops_guru.types.insight_feedback.InsightFeedback"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFeedbackResponse) -> dict:
    out: dict = {}
    if "insight_feedback" in value:
        import capo_devops_guru.types.insight_feedback

        out["InsightFeedback"] = capo_devops_guru.types.insight_feedback.serialize_json(
            value["insight_feedback"]
        )
    return out


def deserialize_json(data: dict) -> DescribeFeedbackResponse:
    out: DescribeFeedbackResponse = {}  # type: ignore[typeddict-item]
    if "InsightFeedback" in data:
        import capo_devops_guru.types.insight_feedback

        out["insight_feedback"] = (
            capo_devops_guru.types.insight_feedback.deserialize_json(
                data["InsightFeedback"]
            )
        )
    return out
