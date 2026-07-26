"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeLanguageCode``."""

from typing import Literal, TypeAlias, cast

MedicalScribeLanguageCode: TypeAlias = Literal["en-US",]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeLanguageCode:
    return cast(MedicalScribeLanguageCode, data)
