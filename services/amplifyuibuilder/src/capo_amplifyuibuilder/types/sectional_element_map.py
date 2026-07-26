"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#SectionalElementMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.sectional_element

SectionalElementMap: TypeAlias = dict[
    "str", "capo_amplifyuibuilder.types.sectional_element.SectionalElement"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SectionalElementMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_amplifyuibuilder.types.sectional_element

        out[key] = capo_amplifyuibuilder.types.sectional_element.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SectionalElementMap:
    out: SectionalElementMap = {}
    for key, value in data.items():
        import capo_amplifyuibuilder.types.sectional_element

        out[key] = capo_amplifyuibuilder.types.sectional_element.deserialize_json(value)
    return out
