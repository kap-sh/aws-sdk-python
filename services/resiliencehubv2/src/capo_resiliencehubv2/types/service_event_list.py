"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_event

ServiceEventList: TypeAlias = list[
    "capo_resiliencehubv2.types.service_event.ServiceEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEventList) -> list:
    import capo_resiliencehubv2.types.service_event

    out: list = []
    for item in value:
        out.append(capo_resiliencehubv2.types.service_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceEventList:
    import capo_resiliencehubv2.types.service_event

    out: ServiceEventList = []
    for item in data:
        out.append(capo_resiliencehubv2.types.service_event.deserialize_json(item))
    return out
