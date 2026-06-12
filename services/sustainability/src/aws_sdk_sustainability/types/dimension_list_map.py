"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionListMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.dimension
    import aws_sdk_sustainability.types.dimension_value_list

DimensionListMap: TypeAlias = dict[
    "aws_sdk_sustainability.types.dimension.Dimension",
    "aws_sdk_sustainability.types.dimension_value_list.DimensionValueList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DimensionListMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sustainability.types.dimension
        import aws_sdk_sustainability.types.dimension_value_list

        out[aws_sdk_sustainability.types.dimension.serialize_json(key)] = (
            aws_sdk_sustainability.types.dimension_value_list.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> DimensionListMap:
    out: DimensionListMap = {}
    for key, value in data.items():
        import aws_sdk_sustainability.types.dimension
        import aws_sdk_sustainability.types.dimension_value_list

        out[aws_sdk_sustainability.types.dimension.deserialize_json(key)] = (
            aws_sdk_sustainability.types.dimension_value_list.deserialize_json(value)
        )
    return out
