"""Generated from Smithy shape ``com.amazonaws.applicationinsights#FeedbackKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

FeedbackKey: TypeAlias = Literal["INSIGHTS_FEEDBACK",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INSIGHTS_FEEDBACK",))


def serialize_aws_json_1_1(value: FeedbackKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeedbackKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeedbackKey value: {data!r}")
    return cast(FeedbackKey, data)
