"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.system_event_type

SystemEventTypeList: TypeAlias = list[
    "capo_resiliencehubv2.types.system_event_type.SystemEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SystemEventTypeList) -> list:
    import capo_resiliencehubv2.types.system_event_type

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.system_event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SystemEventTypeList:
    import capo_resiliencehubv2.types.system_event_type

    out: SystemEventTypeList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.system_event_type.deserialize_json(item))
    return out
