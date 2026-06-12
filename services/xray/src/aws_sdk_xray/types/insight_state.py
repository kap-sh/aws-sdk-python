"""Generated from Smithy shape ``com.amazonaws.xray#InsightState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

InsightState: TypeAlias = Literal[
    "ACTIVE",
    "CLOSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CLOSED",
    )
)


def serialize_json(value: InsightState) -> str:
    return value


def deserialize_json(data: str) -> InsightState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightState value: {data!r}")
    return cast(InsightState, data)
