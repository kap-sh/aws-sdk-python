"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.component

ComponentList: TypeAlias = list["capo_greengrassv2.types.component.Component"]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentList) -> list:
    import capo_greengrassv2.types.component

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentList:
    import capo_greengrassv2.types.component

    out: ComponentList = []
    for item in data:
        out.append(capo_greengrassv2.types.component.deserialize_json(item))
    return out
