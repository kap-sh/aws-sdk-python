"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

TranscribeMedicalContentIdentificationType: TypeAlias = Literal["PHI",]


# --- restJson1 ser/de ---
def serialize_json(value: TranscribeMedicalContentIdentificationType) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalContentIdentificationType:
    return cast(TranscribeMedicalContentIdentificationType, data)
