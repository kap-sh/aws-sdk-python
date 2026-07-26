"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentChildList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_child

ComponentChildList: TypeAlias = list[
    "capo_amplifyuibuilder.types.component_child.ComponentChild"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentChildList) -> list:
    import capo_amplifyuibuilder.types.component_child

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.component_child.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentChildList:
    import capo_amplifyuibuilder.types.component_child

    out: ComponentChildList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.component_child.deserialize_json(item))
    return out
