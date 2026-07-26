"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentsMapRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_path
    import capo_iottwinmaker.types.composite_component_request

CompositeComponentsMapRequest: TypeAlias = dict[
    "capo_iottwinmaker.types.component_path.ComponentPath",
    "capo_iottwinmaker.types.composite_component_request.CompositeComponentRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CompositeComponentsMapRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.composite_component_request

        out[key] = capo_iottwinmaker.types.composite_component_request.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> CompositeComponentsMapRequest:
    out: CompositeComponentsMapRequest = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.composite_component_request

        out[key] = capo_iottwinmaker.types.composite_component_request.deserialize_json(
            value
        )
    return out
