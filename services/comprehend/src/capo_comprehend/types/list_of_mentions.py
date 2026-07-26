"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfMentions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.targeted_sentiment_mention

ListOfMentions: TypeAlias = list[
    "capo_comprehend.types.targeted_sentiment_mention.TargetedSentimentMention"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfMentions) -> list:
    import capo_comprehend.types.targeted_sentiment_mention

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.targeted_sentiment_mention.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfMentions:
    import capo_comprehend.types.targeted_sentiment_mention

    out: ListOfMentions = []
    for item in data:
        out.append(
            capo_comprehend.types.targeted_sentiment_mention.deserialize_aws_json_1_1(
                item
            )
        )
    return out
