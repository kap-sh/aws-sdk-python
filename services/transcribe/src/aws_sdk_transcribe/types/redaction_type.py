"""Generated from Smithy shape ``com.amazonaws.transcribe#RedactionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

RedactionType: TypeAlias = Literal["PII",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PII",))


def serialize_aws_json_1_1(value: RedactionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedactionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RedactionType value: {data!r}")
    return cast(RedactionType, data)
