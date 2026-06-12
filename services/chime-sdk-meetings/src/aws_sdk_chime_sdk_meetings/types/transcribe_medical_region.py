"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeMedicalRegion: TypeAlias = Literal[
    "us-east-1",
    "us-east-2",
    "us-west-2",
    "ap-southeast-2",
    "ca-central-1",
    "eu-west-1",
    "auto",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "us-east-1",
        "us-east-2",
        "us-west-2",
        "ap-southeast-2",
        "ca-central-1",
        "eu-west-1",
        "auto",
    )
)


def serialize_json(value: TranscribeMedicalRegion) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalRegion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscribeMedicalRegion value: {data!r}")
    return cast(TranscribeMedicalRegion, data)
