"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertyPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_property_path_segment

AssetPropertyPath: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_property_path_segment.AssetPropertyPathSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyPath) -> list:
    import aws_sdk_iotsitewise.types.asset_property_path_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.asset_property_path_segment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetPropertyPath:
    import aws_sdk_iotsitewise.types.asset_property_path_segment

    out: AssetPropertyPath = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_property_path_segment.deserialize_json(item)
        )
    return out
