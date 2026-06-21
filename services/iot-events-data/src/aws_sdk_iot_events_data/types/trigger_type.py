"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#TriggerType``."""

from typing import Literal, TypeAlias, cast

TriggerType: TypeAlias = Literal["SNOOZE_TIMEOUT",]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerType) -> str:
    return value


def deserialize_json(data: str) -> TriggerType:
    return cast(TriggerType, data)
