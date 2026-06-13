"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTopicReviewedAnswers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.create_topic_reviewed_answer

CreateTopicReviewedAnswers: TypeAlias = list[
    "aws_sdk_quicksight.types.create_topic_reviewed_answer.CreateTopicReviewedAnswer"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicReviewedAnswers) -> list:
    import aws_sdk_quicksight.types.create_topic_reviewed_answer

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.create_topic_reviewed_answer.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateTopicReviewedAnswers:
    import aws_sdk_quicksight.types.create_topic_reviewed_answer

    out: CreateTopicReviewedAnswers = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.create_topic_reviewed_answer.deserialize_json(item)
        )
    return out
