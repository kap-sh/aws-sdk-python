"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_event_type

ServiceEventTypeList: TypeAlias = list[
    "capo_resiliencehubv2.types.service_event_type.ServiceEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEventTypeList) -> list:
    import capo_resiliencehubv2.types.service_event_type

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.service_event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceEventTypeList:
    import capo_resiliencehubv2.types.service_event_type

    out: ServiceEventTypeList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.service_event_type.deserialize_json(item))
    return out
