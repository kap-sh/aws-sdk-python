"""Generated from Smithy shape ``com.amazonaws.transcribe#SentimentValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.sentiment_value

SentimentValueList: TypeAlias = list[
    "aws_sdk_transcribe.types.sentiment_value.SentimentValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SentimentValueList) -> list:
    import aws_sdk_transcribe.types.sentiment_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe.types.sentiment_value.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SentimentValueList:
    import aws_sdk_transcribe.types.sentiment_value

    out: SentimentValueList = []
    for item in data:
        out.append(
            aws_sdk_transcribe.types.sentiment_value.deserialize_aws_json_1_1(item)
        )
    return out
