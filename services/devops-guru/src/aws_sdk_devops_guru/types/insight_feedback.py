"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightFeedback``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.insight_feedback_option
    import aws_sdk_devops_guru.types.insight_id


class InsightFeedback(TypedDict):
    id: NotRequired["aws_sdk_devops_guru.types.insight_id.InsightId"]
    """<p> The insight feedback ID. </p>"""
    feedback: NotRequired[
        "aws_sdk_devops_guru.types.insight_feedback_option.InsightFeedbackOption"
    ]
    """<p> The feedback provided by the customer. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightFeedback) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "feedback" in value:
        import aws_sdk_devops_guru.types.insight_feedback_option

        out["Feedback"] = (
            aws_sdk_devops_guru.types.insight_feedback_option.serialize_json(
                value["feedback"]
            )
        )
    return out


def deserialize_json(data: dict) -> InsightFeedback:
    out: InsightFeedback = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Feedback" in data:
        import aws_sdk_devops_guru.types.insight_feedback_option

        out["feedback"] = (
            aws_sdk_devops_guru.types.insight_feedback_option.deserialize_json(
                data["Feedback"]
            )
        )
    return out
