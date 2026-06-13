"""Generated from Smithy shape ``com.amazonaws.ssmsap#ReplicationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ReplicationMode: TypeAlias = Literal[
    "PRIMARY",
    "NONE",
    "SYNC",
    "SYNCMEM",
    "ASYNC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "NONE",
        "SYNC",
        "SYNCMEM",
        "ASYNC",
    )
)


def serialize_json(value: ReplicationMode) -> str:
    return value


def deserialize_json(data: str) -> ReplicationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicationMode value: {data!r}")
    return cast(ReplicationMode, data)
