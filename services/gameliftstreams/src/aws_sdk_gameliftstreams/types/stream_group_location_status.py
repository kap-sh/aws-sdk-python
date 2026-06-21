"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamGroupLocationStatus``."""

from typing import Literal, TypeAlias, cast

StreamGroupLocationStatus: TypeAlias = Literal[
    "ACTIVATING",
    "ACTIVE",
    "ERROR",
    "REMOVING",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamGroupLocationStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamGroupLocationStatus:
    return cast(StreamGroupLocationStatus, data)
