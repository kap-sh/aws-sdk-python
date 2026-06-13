"""Generated from Smithy shape ``com.amazonaws.datazone#AssetTypeIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_type_identifier

AssetTypeIdentifiers: TypeAlias = list[
    "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetTypeIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> AssetTypeIdentifiers:
    return list(data)
