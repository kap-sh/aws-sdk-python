"""Generated from Smithy shape ``com.amazonaws.deadline#VolumeState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

"""<p>The state of a persistent volume.</p>"""
VolumeState: TypeAlias = Literal[
    "PENDING_CREATION",
    "PENDING_ATTACHMENT",
    "IN_USE",
    "AVAILABLE",
    "PENDING_DELETION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_CREATION",
        "PENDING_ATTACHMENT",
        "IN_USE",
        "AVAILABLE",
        "PENDING_DELETION",
    )
)


def serialize_json(value: VolumeState) -> str:
    return value


def deserialize_json(data: str) -> VolumeState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeState value: {data!r}")
    return cast(VolumeState, data)
