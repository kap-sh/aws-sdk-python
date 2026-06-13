"""Generated from Smithy shape ``com.amazonaws.datazone#RuleAssetTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_type_identifier

RuleAssetTypeList: TypeAlias = list[
    "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleAssetTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> RuleAssetTypeList:
    return list(data)
