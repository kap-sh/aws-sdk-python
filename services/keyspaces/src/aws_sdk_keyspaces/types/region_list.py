"""Generated from Smithy shape ``com.amazonaws.keyspaces#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.region

RegionList: TypeAlias = list["aws_sdk_keyspaces.types.region.region"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegionList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> RegionList:
    return list(data)
