"""Generated from Smithy shape ``com.amazonaws.fms#AWSRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.aws_region

AWSRegionList: TypeAlias = list["capo_fms.types.aws_region.AWSRegion"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSRegionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AWSRegionList:
    return list(data)
