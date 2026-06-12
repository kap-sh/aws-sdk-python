"""Generated from Smithy shape ``com.amazonaws.transcribe#Rule``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_transcribe.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.interruption_filter
    import aws_sdk_transcribe.types.non_talk_time_filter
    import aws_sdk_transcribe.types.sentiment_filter
    import aws_sdk_transcribe.types.transcript_filter


class _Rule_NonTalkTimeFilter(TypedDict):
    NonTalkTimeFilter: "aws_sdk_transcribe.types.non_talk_time_filter.NonTalkTimeFilter"


class _Rule_InterruptionFilter(TypedDict):
    InterruptionFilter: (
        "aws_sdk_transcribe.types.interruption_filter.InterruptionFilter"
    )


class _Rule_TranscriptFilter(TypedDict):
    TranscriptFilter: "aws_sdk_transcribe.types.transcript_filter.TranscriptFilter"


class _Rule_SentimentFilter(TypedDict):
    SentimentFilter: "aws_sdk_transcribe.types.sentiment_filter.SentimentFilter"


Rule: TypeAlias = (
    _Rule_NonTalkTimeFilter
    | _Rule_InterruptionFilter
    | _Rule_TranscriptFilter
    | _Rule_SentimentFilter
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    if "NonTalkTimeFilter" in value:
        import aws_sdk_transcribe.types.non_talk_time_filter

        return {
            "NonTalkTimeFilter": aws_sdk_transcribe.types.non_talk_time_filter.serialize_aws_json_1_1(
                value["NonTalkTimeFilter"]
            )
        }
    elif "InterruptionFilter" in value:
        import aws_sdk_transcribe.types.interruption_filter

        return {
            "InterruptionFilter": aws_sdk_transcribe.types.interruption_filter.serialize_aws_json_1_1(
                value["InterruptionFilter"]
            )
        }
    elif "TranscriptFilter" in value:
        import aws_sdk_transcribe.types.transcript_filter

        return {
            "TranscriptFilter": aws_sdk_transcribe.types.transcript_filter.serialize_aws_json_1_1(
                value["TranscriptFilter"]
            )
        }
    elif "SentimentFilter" in value:
        import aws_sdk_transcribe.types.sentiment_filter

        return {
            "SentimentFilter": aws_sdk_transcribe.types.sentiment_filter.serialize_aws_json_1_1(
                value["SentimentFilter"]
            )
        }
    else:
        raise SerializationError("Rule: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Rule:
    if "NonTalkTimeFilter" in data:
        import aws_sdk_transcribe.types.non_talk_time_filter

        return {
            "NonTalkTimeFilter": aws_sdk_transcribe.types.non_talk_time_filter.deserialize_aws_json_1_1(
                data["NonTalkTimeFilter"]
            )
        }
    elif "InterruptionFilter" in data:
        import aws_sdk_transcribe.types.interruption_filter

        return {
            "InterruptionFilter": aws_sdk_transcribe.types.interruption_filter.deserialize_aws_json_1_1(
                data["InterruptionFilter"]
            )
        }
    elif "TranscriptFilter" in data:
        import aws_sdk_transcribe.types.transcript_filter

        return {
            "TranscriptFilter": aws_sdk_transcribe.types.transcript_filter.deserialize_aws_json_1_1(
                data["TranscriptFilter"]
            )
        }
    elif "SentimentFilter" in data:
        import aws_sdk_transcribe.types.sentiment_filter

        return {
            "SentimentFilter": aws_sdk_transcribe.types.sentiment_filter.deserialize_aws_json_1_1(
                data["SentimentFilter"]
            )
        }
    else:
        raise DeserializationError("Rule: no recognized variant key")
