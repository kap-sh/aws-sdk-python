"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertyValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_value

AssetPropertyValues: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_property_value.AssetPropertyValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyValues) -> list:
    import aws_sdk_iotsitewise.types.asset_property_value

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.asset_property_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetPropertyValues:
    import aws_sdk_iotsitewise.types.asset_property_value

    out: AssetPropertyValues = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_property_value.deserialize_json(item)
        )
    return out
