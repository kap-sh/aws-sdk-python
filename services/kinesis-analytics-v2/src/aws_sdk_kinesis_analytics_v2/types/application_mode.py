"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

ApplicationMode: TypeAlias = Literal[
    "STREAMING",
    "INTERACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STREAMING",
        "INTERACTIVE",
    )
)


def serialize_aws_json_1_1(value: ApplicationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationMode value: {data!r}")
    return cast(ApplicationMode, data)
