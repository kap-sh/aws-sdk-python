"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

CallAnalyticsFeature: TypeAlias = Literal["GENERATIVE_SUMMARIZATION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GENERATIVE_SUMMARIZATION",))


def serialize_aws_json_1_1(value: CallAnalyticsFeature) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CallAnalyticsFeature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CallAnalyticsFeature value: {data!r}")
    return cast(CallAnalyticsFeature, data)
