"""Generated from Smithy shape ``com.amazonaws.health#EventTypePersonaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_type_persona

EventTypePersonaList: TypeAlias = list[
    "capo_health.types.event_type_persona.EventTypePersona"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypePersonaList) -> list:
    import capo_health.types.event_type_persona

    out: list = []
    for item in value:
        out.append(capo_health.types.event_type_persona.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventTypePersonaList:
    import capo_health.types.event_type_persona

    out: EventTypePersonaList = []
    for item in data:
        out.append(capo_health.types.event_type_persona.deserialize_aws_json_1_1(item))
    return out
