"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQueryState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

ScheduledQueryState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: ScheduledQueryState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScheduledQueryState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScheduledQueryState value: {data!r}")
    return cast(ScheduledQueryState, data)
