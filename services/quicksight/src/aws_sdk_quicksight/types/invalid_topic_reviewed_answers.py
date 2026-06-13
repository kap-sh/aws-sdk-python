"""Generated from Smithy shape ``com.amazonaws.quicksight#InvalidTopicReviewedAnswers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.invalid_topic_reviewed_answer

InvalidTopicReviewedAnswers: TypeAlias = list[
    "aws_sdk_quicksight.types.invalid_topic_reviewed_answer.InvalidTopicReviewedAnswer"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidTopicReviewedAnswers) -> list:
    import aws_sdk_quicksight.types.invalid_topic_reviewed_answer

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.invalid_topic_reviewed_answer.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InvalidTopicReviewedAnswers:
    import aws_sdk_quicksight.types.invalid_topic_reviewed_answer

    out: InvalidTopicReviewedAnswers = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.invalid_topic_reviewed_answer.deserialize_json(
                item
            )
        )
    return out
