"""Generated from Smithy shape ``com.amazonaws.ssm#CalendarState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

CalendarState: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "CLOSED",
    )
)


def serialize_aws_json_1_1(value: CalendarState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CalendarState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CalendarState value: {data!r}")
    return cast(CalendarState, data)
