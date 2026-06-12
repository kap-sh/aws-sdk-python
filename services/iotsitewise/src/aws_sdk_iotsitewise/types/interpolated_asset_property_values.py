"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterpolatedAssetPropertyValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.interpolated_asset_property_value

InterpolatedAssetPropertyValues: TypeAlias = list[
    "aws_sdk_iotsitewise.types.interpolated_asset_property_value.InterpolatedAssetPropertyValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: InterpolatedAssetPropertyValues) -> list:
    import aws_sdk_iotsitewise.types.interpolated_asset_property_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.interpolated_asset_property_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InterpolatedAssetPropertyValues:
    import aws_sdk_iotsitewise.types.interpolated_asset_property_value

    out: InterpolatedAssetPropertyValues = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.interpolated_asset_property_value.deserialize_json(
                item
            )
        )
    return out
