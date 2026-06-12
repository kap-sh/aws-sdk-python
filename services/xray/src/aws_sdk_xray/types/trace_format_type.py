"""Generated from Smithy shape ``com.amazonaws.xray#TraceFormatType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

TraceFormatType: TypeAlias = Literal[
    "XRAY",
    "OTEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "XRAY",
        "OTEL",
    )
)


def serialize_json(value: TraceFormatType) -> str:
    return value


def deserialize_json(data: str) -> TraceFormatType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TraceFormatType value: {data!r}")
    return cast(TraceFormatType, data)
