"""Generated from Smithy shape ``com.amazonaws.novaact#ActStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_nova_act.errors import DeserializationError

ActStatus: TypeAlias = Literal[
    "RUNNING",
    "PENDING_CLIENT_ACTION",
    "PENDING_HUMAN_ACTION",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "PENDING_CLIENT_ACTION",
        "PENDING_HUMAN_ACTION",
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
    )
)


def serialize_json(value: ActStatus) -> str:
    return value


def deserialize_json(data: str) -> ActStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActStatus value: {data!r}")
    return cast(ActStatus, data)
