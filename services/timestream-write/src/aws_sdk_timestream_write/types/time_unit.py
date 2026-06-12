"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#TimeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

TimeUnit: TypeAlias = Literal[
    "MILLISECONDS",
    "SECONDS",
    "MICROSECONDS",
    "NANOSECONDS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MILLISECONDS",
        "SECONDS",
        "MICROSECONDS",
        "NANOSECONDS",
    )
)


def serialize_aws_json_1_0(value: TimeUnit) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TimeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeUnit value: {data!r}")
    return cast(TimeUnit, data)
