"""Generated from Smithy shape ``com.amazonaws.datazone#AwsRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.aws_region

AwsRegionList: TypeAlias = list["capo_datazone.types.aws_region.AwsRegion"]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> AwsRegionList:
    return list(data)
