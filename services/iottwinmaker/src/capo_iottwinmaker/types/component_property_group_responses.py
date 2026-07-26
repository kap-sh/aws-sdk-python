"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentPropertyGroupResponses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_property_group_response
    import capo_iottwinmaker.types.name

ComponentPropertyGroupResponses: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.component_property_group_response.ComponentPropertyGroupResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentPropertyGroupResponses) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.component_property_group_response

        out[key] = (
            capo_iottwinmaker.types.component_property_group_response.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentPropertyGroupResponses:
    out: ComponentPropertyGroupResponses = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.component_property_group_response

        out[key] = (
            capo_iottwinmaker.types.component_property_group_response.deserialize_json(
                value
            )
        )
    return out
