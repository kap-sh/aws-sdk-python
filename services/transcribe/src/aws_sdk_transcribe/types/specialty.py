"""Generated from Smithy shape ``com.amazonaws.transcribe#Specialty``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

Specialty: TypeAlias = Literal["PRIMARYCARE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PRIMARYCARE",))


def serialize_aws_json_1_1(value: Specialty) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Specialty:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Specialty value: {data!r}")
    return cast(Specialty, data)
