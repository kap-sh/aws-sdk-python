"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

StreamGroupStatus: TypeAlias = Literal[
    "ACTIVATING",
    "UPDATING_LOCATIONS",
    "ACTIVE",
    "ACTIVE_WITH_ERRORS",
    "ERROR",
    "DELETING",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVATING",
        "UPDATING_LOCATIONS",
        "ACTIVE",
        "ACTIVE_WITH_ERRORS",
        "ERROR",
        "DELETING",
        "EXPIRED",
    )
)


def serialize_json(value: StreamGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamGroupStatus value: {data!r}")
    return cast(StreamGroupStatus, data)
