"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ReplicationStatusType``."""

from typing import Literal, TypeAlias, cast

ReplicationStatusType: TypeAlias = Literal[
    "REPLICATING",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatusType) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStatusType:
    return cast(ReplicationStatusType, data)
