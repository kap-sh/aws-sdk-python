"""Generated from Smithy shape ``com.amazonaws.kendra#RelevanceFeedbackList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.relevance_feedback

RelevanceFeedbackList: TypeAlias = list[
    "capo_kendra.types.relevance_feedback.RelevanceFeedback"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelevanceFeedbackList) -> list:
    import capo_kendra.types.relevance_feedback

    out: list = []
    for item in value:
        out.append(capo_kendra.types.relevance_feedback.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RelevanceFeedbackList:
    import capo_kendra.types.relevance_feedback

    out: RelevanceFeedbackList = []
    for item in data:
        out.append(capo_kendra.types.relevance_feedback.deserialize_aws_json_1_1(item))
    return out
