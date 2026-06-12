"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

TelemetryState: TypeAlias = Literal[
    "Enabled",
    "Disabled",
    "NotApplicable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
        "NotApplicable",
    )
)


def serialize_json(value: TelemetryState) -> str:
    return value


def deserialize_json(data: str) -> TelemetryState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TelemetryState value: {data!r}")
    return cast(TelemetryState, data)
