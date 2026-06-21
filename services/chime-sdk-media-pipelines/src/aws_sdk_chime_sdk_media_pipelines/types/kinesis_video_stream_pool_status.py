"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamPoolStatus``."""

from typing import Literal, TypeAlias, cast

KinesisVideoStreamPoolStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamPoolStatus) -> str:
    return value


def deserialize_json(data: str) -> KinesisVideoStreamPoolStatus:
    return cast(KinesisVideoStreamPoolStatus, data)
