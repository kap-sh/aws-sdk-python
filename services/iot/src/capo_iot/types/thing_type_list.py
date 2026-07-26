"""Generated from Smithy shape ``com.amazonaws.iot#ThingTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.thing_type_definition

ThingTypeList: TypeAlias = list[
    "capo_iot.types.thing_type_definition.ThingTypeDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingTypeList) -> list:
    import capo_iot.types.thing_type_definition

    out: list = []
    for item in value:
        out.append(capo_iot.types.thing_type_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThingTypeList:
    import capo_iot.types.thing_type_definition

    out: ThingTypeList = []
    for item in data:
        out.append(capo_iot.types.thing_type_definition.deserialize_json(item))
    return out
