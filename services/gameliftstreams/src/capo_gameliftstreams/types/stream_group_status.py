"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamGroupStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: StreamGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamGroupStatus:
    return cast(StreamGroupStatus, data)
