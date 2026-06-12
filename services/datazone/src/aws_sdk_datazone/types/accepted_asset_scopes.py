"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptedAssetScopes``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.accepted_asset_scope

AcceptedAssetScopes: TypeAlias = list["aws_sdk_datazone.types.accepted_asset_scope.AcceptedAssetScope"]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptedAssetScopes) -> list:
    import aws_sdk_datazone.types.accepted_asset_scope
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.accepted_asset_scope.serialize_json(item))
    return out


def deserialize_json(data: list) -> AcceptedAssetScopes:
    import aws_sdk_datazone.types.accepted_asset_scope
    out: AcceptedAssetScopes = []
    for item in data:
        out.append(aws_sdk_datazone.types.accepted_asset_scope.deserialize_json(item))
    return out