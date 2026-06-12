"""Generated from Smithy shape ``com.amazonaws.datazone#ApplicableAssetTypes``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.type_name

ApplicableAssetTypes: TypeAlias = list["aws_sdk_datazone.types.type_name.TypeName"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicableAssetTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> ApplicableAssetTypes:
    return list(data)