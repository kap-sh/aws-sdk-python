"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetHierarchies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_hierarchy

AssetHierarchies: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_hierarchy.AssetHierarchy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetHierarchies) -> list:
    import aws_sdk_iotsitewise.types.asset_hierarchy

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.asset_hierarchy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetHierarchies:
    import aws_sdk_iotsitewise.types.asset_hierarchy

    out: AssetHierarchies = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.asset_hierarchy.deserialize_json(item))
    return out
