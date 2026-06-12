"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

MedicalScribeLanguageCode: TypeAlias = Literal["en-US",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("en-US",))


def serialize_aws_json_1_1(value: MedicalScribeLanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalScribeLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MedicalScribeLanguageCode value: {data!r}")
    return cast(MedicalScribeLanguageCode, data)
