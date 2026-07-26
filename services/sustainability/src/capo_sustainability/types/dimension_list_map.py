"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionListMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sustainability.types.dimension
    import capo_sustainability.types.dimension_value_list

DimensionListMap: TypeAlias = dict[
    "capo_sustainability.types.dimension.Dimension",
    "capo_sustainability.types.dimension_value_list.DimensionValueList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DimensionListMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sustainability.types.dimension
        import capo_sustainability.types.dimension_value_list

        out[capo_sustainability.types.dimension.serialize_json(key)] = (
            capo_sustainability.types.dimension_value_list.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> DimensionListMap:
    out: DimensionListMap = {}
    for key, value in data.items():
        import capo_sustainability.types.dimension
        import capo_sustainability.types.dimension_value_list

        out[capo_sustainability.types.dimension.deserialize_json(key)] = (
            capo_sustainability.types.dimension_value_list.deserialize_json(value)
        )
    return out
