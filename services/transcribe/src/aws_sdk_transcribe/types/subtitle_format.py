"""Generated from Smithy shape ``com.amazonaws.transcribe#SubtitleFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

SubtitleFormat: TypeAlias = Literal[
    "vtt",
    "srt",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "vtt",
        "srt",
    )
)


def serialize_aws_json_1_1(value: SubtitleFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubtitleFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubtitleFormat value: {data!r}")
    return cast(SubtitleFormat, data)
