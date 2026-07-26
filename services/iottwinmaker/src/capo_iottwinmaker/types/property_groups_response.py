"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyGroupsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.property_group_response

PropertyGroupsResponse: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name",
    "capo_iottwinmaker.types.property_group_response.PropertyGroupResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PropertyGroupsResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iottwinmaker.types.property_group_response

        out[key] = capo_iottwinmaker.types.property_group_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PropertyGroupsResponse:
    out: PropertyGroupsResponse = {}
    for key, value in data.items():
        import capo_iottwinmaker.types.property_group_response

        out[key] = capo_iottwinmaker.types.property_group_response.deserialize_json(
            value
        )
    return out
