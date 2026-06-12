"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

TranscriptFilterType: TypeAlias = Literal["EXACT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EXACT",))


def serialize_aws_json_1_1(value: TranscriptFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TranscriptFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscriptFilterType value: {data!r}")
    return cast(TranscriptFilterType, data)
