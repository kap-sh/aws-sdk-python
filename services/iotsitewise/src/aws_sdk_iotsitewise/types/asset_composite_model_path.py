"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetCompositeModelPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.asset_composite_model_path_segment

AssetCompositeModelPath: TypeAlias = list[
    "aws_sdk_iotsitewise.types.asset_composite_model_path_segment.AssetCompositeModelPathSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetCompositeModelPath) -> list:
    import aws_sdk_iotsitewise.types.asset_composite_model_path_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.asset_composite_model_path_segment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetCompositeModelPath:
    import aws_sdk_iotsitewise.types.asset_composite_model_path_segment

    out: AssetCompositeModelPath = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.asset_composite_model_path_segment.deserialize_json(
                item
            )
        )
    return out
