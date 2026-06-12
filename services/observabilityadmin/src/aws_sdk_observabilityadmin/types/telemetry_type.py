"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

TelemetryType: TypeAlias = Literal[
    "Logs",
    "Metrics",
    "Traces",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Logs",
        "Metrics",
        "Traces",
    )
)


def serialize_json(value: TelemetryType) -> str:
    return value


def deserialize_json(data: str) -> TelemetryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TelemetryType value: {data!r}")
    return cast(TelemetryType, data)
