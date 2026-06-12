"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventIngestion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

EventIngestion: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: EventIngestion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventIngestion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventIngestion value: {data!r}")
    return cast(EventIngestion, data)
