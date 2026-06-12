"""Generated from Smithy shape ``com.amazonaws.uxc#RegionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_uxc.types.region

RegionsList: TypeAlias = list["aws_sdk_uxc.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: RegionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegionsList:
    return list(data)
