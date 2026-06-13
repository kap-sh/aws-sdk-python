"""Generated from Smithy shape ``com.amazonaws.location#CustomLayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.custom_layer

CustomLayerList: TypeAlias = list["aws_sdk_location.types.custom_layer.CustomLayer"]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLayerList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomLayerList:
    return list(data)
