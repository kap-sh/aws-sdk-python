"""Generated from Smithy shape ``com.amazonaws.ssmsap#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ClusterStatus: TypeAlias = Literal[
    "ONLINE",
    "STANDBY",
    "MAINTENANCE",
    "OFFLINE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONLINE",
        "STANDBY",
        "MAINTENANCE",
        "OFFLINE",
        "NONE",
    )
)


def serialize_json(value: ClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> ClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterStatus value: {data!r}")
    return cast(ClusterStatus, data)
