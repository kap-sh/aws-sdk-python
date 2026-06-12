"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateNodeStateShape``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in UpdateNodeStateRequest."""
UpdateNodeStateShape: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DRAINING",
    )
)


def serialize_json(value: UpdateNodeStateShape) -> str:
    return value


def deserialize_json(data: str) -> UpdateNodeStateShape:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateNodeStateShape value: {data!r}")
    return cast(UpdateNodeStateShape, data)
