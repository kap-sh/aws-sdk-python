"""Generated from Smithy shape ``com.amazonaws.quicksight#SucceededTopicReviewedAnswers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.succeeded_topic_reviewed_answer

SucceededTopicReviewedAnswers: TypeAlias = list[
    "capo_quicksight.types.succeeded_topic_reviewed_answer.SucceededTopicReviewedAnswer"
]


# --- restJson1 ser/de ---
def serialize_json(value: SucceededTopicReviewedAnswers) -> list:
    import capo_quicksight.types.succeeded_topic_reviewed_answer

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.succeeded_topic_reviewed_answer.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SucceededTopicReviewedAnswers:
    import capo_quicksight.types.succeeded_topic_reviewed_answer

    out: SucceededTopicReviewedAnswers = []
    for item in data:
        out.append(
            capo_quicksight.types.succeeded_topic_reviewed_answer.deserialize_json(item)
        )
    return out
