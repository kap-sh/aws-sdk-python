"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmModelVersionStatus``."""

from typing import Literal, TypeAlias, cast

AlarmModelVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "ACTIVATING",
    "INACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmModelVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> AlarmModelVersionStatus:
    return cast(AlarmModelVersionStatus, data)
