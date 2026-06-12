"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

MedicalContentIdentificationType: TypeAlias = Literal["PHI",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PHI",))


def serialize_aws_json_1_1(value: MedicalContentIdentificationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalContentIdentificationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MedicalContentIdentificationType value: {data!r}"
        )
    return cast(MedicalContentIdentificationType, data)
