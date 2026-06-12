"""Generated from Smithy shape ``com.amazonaws.medialive#M3u8KlvBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M3u8 Klv Behavior"""
M3u8KlvBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_PASSTHROUGH",
        "PASSTHROUGH",
    )
)


def serialize_json(value: M3u8KlvBehavior) -> str:
    return value


def deserialize_json(data: str) -> M3u8KlvBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M3u8KlvBehavior value: {data!r}")
    return cast(M3u8KlvBehavior, data)
