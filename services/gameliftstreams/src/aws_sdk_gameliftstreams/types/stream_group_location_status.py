"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamGroupLocationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

StreamGroupLocationStatus: TypeAlias = Literal[
    "ACTIVATING",
    "ACTIVE",
    "ERROR",
    "REMOVING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVATING",
        "ACTIVE",
        "ERROR",
        "REMOVING",
    )
)


def serialize_json(value: StreamGroupLocationStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamGroupLocationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamGroupLocationStatus value: {data!r}")
    return cast(StreamGroupLocationStatus, data)
