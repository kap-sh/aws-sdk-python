"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id

AssetIDs: TypeAlias = list["aws_sdk_iotsitewise.types.id.ID"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> AssetIDs:
    return list(data)
