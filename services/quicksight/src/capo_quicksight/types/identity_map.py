"""Generated from Smithy shape ``com.amazonaws.quicksight#IdentityMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.identity_name_list
    import capo_quicksight.types.string

IdentityMap: TypeAlias = dict[
    "capo_quicksight.types.string.String",
    "capo_quicksight.types.identity_name_list.IdentityNameList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: IdentityMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.identity_name_list

        out[key] = capo_quicksight.types.identity_name_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> IdentityMap:
    out: IdentityMap = {}
    for key, value in data.items():
        import capo_quicksight.types.identity_name_list

        out[key] = capo_quicksight.types.identity_name_list.deserialize_json(value)
    return out
