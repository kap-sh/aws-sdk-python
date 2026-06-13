"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeSessionControlEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

MedicalScribeSessionControlEventType: TypeAlias = Literal["END_OF_SESSION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("END_OF_SESSION",))


def serialize_json(value: MedicalScribeSessionControlEventType) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeSessionControlEventType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MedicalScribeSessionControlEventType value: {data!r}"
        )
    return cast(MedicalScribeSessionControlEventType, data)
