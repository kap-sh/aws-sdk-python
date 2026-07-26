"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentUpdatesMapRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_update_request
    import capo_iottwinmaker.types.name

ComponentUpdatesMapRequest: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.component_update_request.ComponentUpdateRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentUpdatesMapRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.component_update_request

        out[key] = capo_iottwinmaker.types.component_update_request.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ComponentUpdatesMapRequest:
    out: ComponentUpdatesMapRequest = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.component_update_request

        out[key] = capo_iottwinmaker.types.component_update_request.deserialize_json(
            value
        )
    return out
