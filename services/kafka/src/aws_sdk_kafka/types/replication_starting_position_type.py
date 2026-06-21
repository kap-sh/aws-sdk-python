"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationStartingPositionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of replication starting position.</p>"""
ReplicationStartingPositionType: TypeAlias = Literal[
    "LATEST",
    "EARLIEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStartingPositionType) -> str:
    return value


def deserialize_json(data: str) -> ReplicationStartingPositionType:
    return cast(ReplicationStartingPositionType, data)
