"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

MedicalContentIdentificationType: TypeAlias = Literal["PHI",]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalContentIdentificationType) -> str:
    return value


def deserialize_json(data: str) -> MedicalContentIdentificationType:
    return cast(MedicalContentIdentificationType, data)
