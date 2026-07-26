"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__listOf__PeriodTriggersElement``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__period_triggers_element

__listOf__PeriodTriggersElement: TypeAlias = list[
    "capo_mediapackage_vod.types.__period_triggers_element.__PeriodTriggersElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__PeriodTriggersElement) -> list:
    import capo_mediapackage_vod.types.__period_triggers_element

    out: list = []
    for item in value:
        out.append(
            capo_mediapackage_vod.types.__period_triggers_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOf__PeriodTriggersElement:
    import capo_mediapackage_vod.types.__period_triggers_element

    out: __listOf__PeriodTriggersElement = []
    for item in data:
        out.append(
            capo_mediapackage_vod.types.__period_triggers_element.deserialize_json(item)
        )
    return out
