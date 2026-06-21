"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalLanguageCode``."""

from typing import Literal, TypeAlias, cast

TranscribeMedicalLanguageCode: TypeAlias = Literal["en-US",]


# --- restJson1 ser/de ---
def serialize_json(value: TranscribeMedicalLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalLanguageCode:
    return cast(TranscribeMedicalLanguageCode, data)
