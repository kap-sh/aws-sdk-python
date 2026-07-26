"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CompositeComponentUpdatesMapRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_path
    import capo_iottwinmaker.types.composite_component_update_request

CompositeComponentUpdatesMapRequest: TypeAlias = dict[
    "capo_iottwinmaker.types.component_path.ComponentPath",
    "capo_iottwinmaker.types.composite_component_update_request.CompositeComponentUpdateRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CompositeComponentUpdatesMapRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.composite_component_update_request

        out[key] = (
            capo_iottwinmaker.types.composite_component_update_request.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CompositeComponentUpdatesMapRequest:
    out: CompositeComponentUpdatesMapRequest = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.composite_component_update_request

        out[key] = (
            capo_iottwinmaker.types.composite_component_update_request.deserialize_json(
                value
            )
        )
    return out
