"""Generated from Smithy shape ``com.amazonaws.connect#AnsweringMachineDetectionStatus``."""

from typing import Literal, TypeAlias, cast

AnsweringMachineDetectionStatus: TypeAlias = Literal[
    "ANSWERED",
    "UNDETECTED",
    "ERROR",
    "HUMAN_ANSWERED",
    "SIT_TONE_DETECTED",
    "SIT_TONE_BUSY",
    "SIT_TONE_INVALID_NUMBER",
    "FAX_MACHINE_DETECTED",
    "VOICEMAIL_BEEP",
    "VOICEMAIL_NO_BEEP",
    "AMD_UNRESOLVED",
    "AMD_UNANSWERED",
    "AMD_ERROR",
    "AMD_NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnsweringMachineDetectionStatus) -> str:
    return value


def deserialize_json(data: str) -> AnsweringMachineDetectionStatus:
    return cast(AnsweringMachineDetectionStatus, data)
