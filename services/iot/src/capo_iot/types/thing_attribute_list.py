"""Generated from Smithy shape ``com.amazonaws.iot#ThingAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.thing_attribute

ThingAttributeList: TypeAlias = list["capo_iot.types.thing_attribute.ThingAttribute"]


# --- restJson1 ser/de ---
def serialize_json(value: ThingAttributeList) -> list:
    import capo_iot.types.thing_attribute

    out: list = []
    for item in value:
        out.append(capo_iot.types.thing_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThingAttributeList:
    import capo_iot.types.thing_attribute

    out: ThingAttributeList = []
    for item in data:
        out.append(capo_iot.types.thing_attribute.deserialize_json(item))
    return out
