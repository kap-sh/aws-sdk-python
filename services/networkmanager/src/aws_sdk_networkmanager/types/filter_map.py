"""Generated from Smithy shape ``com.amazonaws.networkmanager#FilterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.filter_name
    import aws_sdk_networkmanager.types.filter_values

FilterMap: TypeAlias = dict[
    "aws_sdk_networkmanager.types.filter_name.FilterName",
    "aws_sdk_networkmanager.types.filter_values.FilterValues",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FilterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_networkmanager.types.filter_values

        out[key] = aws_sdk_networkmanager.types.filter_values.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FilterMap:
    out: FilterMap = {}
    for key, value in data.items():
        import aws_sdk_networkmanager.types.filter_values

        out[key] = aws_sdk_networkmanager.types.filter_values.deserialize_json(value)
    return out
