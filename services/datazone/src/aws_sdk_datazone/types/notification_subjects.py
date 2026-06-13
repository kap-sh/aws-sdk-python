"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationSubjects``."""

from typing import TypeAlias

NotificationSubjects: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSubjects) -> list:
    return list(value)


def deserialize_json(data: list) -> NotificationSubjects:
    return list(data)
