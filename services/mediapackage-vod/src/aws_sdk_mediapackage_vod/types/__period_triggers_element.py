"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__PeriodTriggersElement``."""

from typing import Literal, TypeAlias, cast

__PeriodTriggersElement: TypeAlias = Literal["ADS",]


# --- restJson1 ser/de ---
def serialize_json(value: __PeriodTriggersElement) -> str:
    return value


def deserialize_json(data: str) -> __PeriodTriggersElement:
    return cast(__PeriodTriggersElement, data)
