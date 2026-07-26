"""Generated from Smithy shape ``com.amazonaws.ssmincidents#EventReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.event_reference

EventReferenceList: TypeAlias = list[
    "capo_ssm_incidents.types.event_reference.EventReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventReferenceList) -> list:
    import capo_ssm_incidents.types.event_reference

    out: list = []
    for item in value:
        out.append(capo_ssm_incidents.types.event_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventReferenceList:
    import capo_ssm_incidents.types.event_reference

    out: EventReferenceList = []
    for item in data:
        out.append(capo_ssm_incidents.types.event_reference.deserialize_json(item))
    return out
