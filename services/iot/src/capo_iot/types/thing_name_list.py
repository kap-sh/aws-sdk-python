"""Generated from Smithy shape ``com.amazonaws.iot#ThingNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.thing_name

ThingNameList: TypeAlias = list["capo_iot.types.thing_name.ThingName"]


# --- restJson1 ser/de ---
def serialize_json(value: ThingNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ThingNameList:
    return list(data)
