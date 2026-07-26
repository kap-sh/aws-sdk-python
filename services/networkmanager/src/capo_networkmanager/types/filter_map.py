"""Generated from Smithy shape ``com.amazonaws.networkmanager#FilterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.filter_name
    import capo_networkmanager.types.filter_values

FilterMap: TypeAlias = dict[
    "capo_networkmanager.types.filter_name.FilterName",
    "capo_networkmanager.types.filter_values.FilterValues",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FilterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_networkmanager.types.filter_values

        out[key] = capo_networkmanager.types.filter_values.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FilterMap:
    out: FilterMap = {}
    for key, value in data.items():
        import capo_networkmanager.types.filter_values

        out[key] = capo_networkmanager.types.filter_values.deserialize_json(value)
    return out
