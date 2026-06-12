"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipelineStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

TelemetryPipelineStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "CREATE_FAILED",
        "UPDATE_FAILED",
    )
)


def serialize_json(value: TelemetryPipelineStatus) -> str:
    return value


def deserialize_json(data: str) -> TelemetryPipelineStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TelemetryPipelineStatus value: {data!r}")
    return cast(TelemetryPipelineStatus, data)
