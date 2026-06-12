"""Generated from Smithy shape ``com.amazonaws.pi#PeriodAlignment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

PeriodAlignment: TypeAlias = Literal[
    "END_TIME",
    "START_TIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "END_TIME",
        "START_TIME",
    )
)


def serialize_aws_json_1_1(value: PeriodAlignment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PeriodAlignment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PeriodAlignment value: {data!r}")
    return cast(PeriodAlignment, data)
