"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

TimeUnit: TypeAlias = Literal[
    "MILLISECOND",
    "SECOND",
    "MINUTE",
    "HOUR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MILLISECOND",
        "SECOND",
        "MINUTE",
        "HOUR",
    )
)


def serialize_aws_json_1_0(value: TimeUnit) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TimeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeUnit value: {data!r}")
    return cast(TimeUnit, data)
