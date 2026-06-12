"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamPoolStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

KinesisVideoStreamPoolStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: KinesisVideoStreamPoolStatus) -> str:
    return value


def deserialize_json(data: str) -> KinesisVideoStreamPoolStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KinesisVideoStreamPoolStatus value: {data!r}"
        )
    return cast(KinesisVideoStreamPoolStatus, data)
