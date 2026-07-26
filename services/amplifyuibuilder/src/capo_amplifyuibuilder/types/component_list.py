"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component

ComponentList: TypeAlias = list["capo_amplifyuibuilder.types.component.Component"]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentList) -> list:
    import capo_amplifyuibuilder.types.component

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentList:
    import capo_amplifyuibuilder.types.component

    out: ComponentList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.component.deserialize_json(item))
    return out
