"""Generated from Smithy shape ``com.amazonaws.iot#PropagatingAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.propagating_attribute

PropagatingAttributeList: TypeAlias = list[
    "capo_iot.types.propagating_attribute.PropagatingAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropagatingAttributeList) -> list:
    import capo_iot.types.propagating_attribute

    out: list = []
    for item in value:
        out.append(capo_iot.types.propagating_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> PropagatingAttributeList:
    import capo_iot.types.propagating_attribute

    out: PropagatingAttributeList = []
    for item in data:
        out.append(capo_iot.types.propagating_attribute.deserialize_json(item))
    return out
