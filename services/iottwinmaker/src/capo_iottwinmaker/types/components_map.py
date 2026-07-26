"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_response
    import capo_iottwinmaker.types.name

ComponentsMap: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.component_response.ComponentResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.component_response

        out[key] = capo_iottwinmaker.types.component_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ComponentsMap:
    out: ComponentsMap = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.component_response

        out[key] = capo_iottwinmaker.types.component_response.deserialize_json(value)
    return out
