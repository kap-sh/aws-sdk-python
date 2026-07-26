"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalRegion``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: TranscribeMedicalRegion) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalRegion:
    return cast(TranscribeMedicalRegion, data)
