"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.system_event

SystemEventList: TypeAlias = list["capo_resiliencehubv2.types.system_event.SystemEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: SystemEventList) -> list:
    import capo_resiliencehubv2.types.system_event

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.system_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> SystemEventList:
    import capo_resiliencehubv2.types.system_event

    out: SystemEventList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.system_event.deserialize_json(item))
    return out
