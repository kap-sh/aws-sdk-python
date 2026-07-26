"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleRestrictiveResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_restrictive_resource_id

AssetBundleRestrictiveResourceIdList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_restrictive_resource_id.AssetBundleRestrictiveResourceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleRestrictiveResourceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssetBundleRestrictiveResourceIdList:
    return list(data)
