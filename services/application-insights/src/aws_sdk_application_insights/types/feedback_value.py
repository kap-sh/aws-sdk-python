"""Generated from Smithy shape ``com.amazonaws.applicationinsights#FeedbackValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

FeedbackValue: TypeAlias = Literal[
    "NOT_SPECIFIED",
    "USEFUL",
    "NOT_USEFUL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_SPECIFIED",
        "USEFUL",
        "NOT_USEFUL",
    )
)


def serialize_aws_json_1_1(value: FeedbackValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeedbackValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeedbackValue value: {data!r}")
    return cast(FeedbackValue, data)
