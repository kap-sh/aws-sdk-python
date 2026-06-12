"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeRegion: TypeAlias = Literal[
    "us-east-2",
    "us-east-1",
    "us-west-2",
    "ap-northeast-2",
    "ap-southeast-2",
    "ap-northeast-1",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "sa-east-1",
    "auto",
    "us-gov-west-1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "us-east-2",
        "us-east-1",
        "us-west-2",
        "ap-northeast-2",
        "ap-southeast-2",
        "ap-northeast-1",
        "ca-central-1",
        "eu-central-1",
        "eu-west-1",
        "eu-west-2",
        "sa-east-1",
        "auto",
        "us-gov-west-1",
    )
)


def serialize_json(value: TranscribeRegion) -> str:
    return value


def deserialize_json(data: str) -> TranscribeRegion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscribeRegion value: {data!r}")
    return cast(TranscribeRegion, data)
