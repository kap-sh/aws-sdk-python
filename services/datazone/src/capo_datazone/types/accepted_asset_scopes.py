"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptedAssetScopes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.accepted_asset_scope

AcceptedAssetScopes: TypeAlias = list[
    "capo_datazone.types.accepted_asset_scope.AcceptedAssetScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptedAssetScopes) -> list:
    import capo_datazone.types.accepted_asset_scope

    out: list = []
    for item in value:
        out.append(capo_datazone.types.accepted_asset_scope.serialize_json(item))
    return out


def deserialize_json(data: list) -> AcceptedAssetScopes:
    import capo_datazone.types.accepted_asset_scope

    out: AcceptedAssetScopes = []
    for item in data:
        out.append(capo_datazone.types.accepted_asset_scope.deserialize_json(item))
    return out
