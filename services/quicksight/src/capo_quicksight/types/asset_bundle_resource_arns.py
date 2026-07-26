"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.arn

AssetBundleResourceArns: TypeAlias = list["capo_quicksight.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleResourceArns) -> list:
    return list(value)


def deserialize_json(data: list) -> AssetBundleResourceArns:
    return list(data)
