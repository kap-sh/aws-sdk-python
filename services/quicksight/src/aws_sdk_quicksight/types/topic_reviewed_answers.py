"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicReviewedAnswers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_reviewed_answer

TopicReviewedAnswers: TypeAlias = list[
    "aws_sdk_quicksight.types.topic_reviewed_answer.TopicReviewedAnswer"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicReviewedAnswers) -> list:
    import aws_sdk_quicksight.types.topic_reviewed_answer

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_reviewed_answer.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicReviewedAnswers:
    import aws_sdk_quicksight.types.topic_reviewed_answer

    out: TopicReviewedAnswers = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.topic_reviewed_answer.deserialize_json(item)
        )
    return out
