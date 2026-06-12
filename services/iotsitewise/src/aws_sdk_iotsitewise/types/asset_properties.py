"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property

AssetProperties: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_property.AssetProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetProperties) -> list:
    import aws_sdk_iotsitewise.types.asset_property

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.asset_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetProperties:
    import aws_sdk_iotsitewise.types.asset_property

    out: AssetProperties = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.asset_property.deserialize_json(item))
    return out
