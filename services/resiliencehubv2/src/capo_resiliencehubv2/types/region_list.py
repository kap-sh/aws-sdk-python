"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.aws_region

RegionList: TypeAlias = list["capo_resiliencehubv2.types.aws_region.AwsRegion"]


# --- restJson1 ser/de ---
def serialize_json(value: RegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegionList:
    return list(data)
