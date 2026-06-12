"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryEnrichmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

TelemetryEnrichmentStatus: TypeAlias = Literal[
    "Running",
    "Stopped",
    "Impaired",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Running",
        "Stopped",
        "Impaired",
    )
)


def serialize_json(value: TelemetryEnrichmentStatus) -> str:
    return value


def deserialize_json(data: str) -> TelemetryEnrichmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TelemetryEnrichmentStatus value: {data!r}")
    return cast(TelemetryEnrichmentStatus, data)
