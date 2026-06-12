"""Generated from Smithy shape ``com.amazonaws.controltower#TargetRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.region

TargetRegions: TypeAlias = list["aws_sdk_controltower.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetRegions) -> list:
    import aws_sdk_controltower.types.region

    out: list = []
    for item in value:
        out.append(aws_sdk_controltower.types.region.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetRegions:
    import aws_sdk_controltower.types.region

    out: TargetRegions = []
    for item in data:
        out.append(aws_sdk_controltower.types.region.deserialize_json(item))
    return out
