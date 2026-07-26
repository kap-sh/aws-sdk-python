"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyGroupsRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.property_group_request

PropertyGroupsRequest: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.property_group_request.PropertyGroupRequest",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyGroupsRequest) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.property_group_request

        out[key] = capo_iottwinmaker.types.property_group_request.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PropertyGroupsRequest:
    out: PropertyGroupsRequest = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.property_group_request

        out[key] = capo_iottwinmaker.types.property_group_request.deserialize_json(
            value
        )
    return out
