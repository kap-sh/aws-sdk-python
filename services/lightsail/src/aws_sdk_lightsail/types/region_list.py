"""Generated from Smithy shape ``com.amazonaws.lightsail#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.region

RegionList: TypeAlias = list["aws_sdk_lightsail.types.region.Region"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionList) -> list:
    import aws_sdk_lightsail.types.region

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.region.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegionList:
    import aws_sdk_lightsail.types.region

    out: RegionList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.region.deserialize_aws_json_1_1(item))
    return out
