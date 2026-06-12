"""Generated from Smithy shape ``com.amazonaws.dax#AvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dax.types.string

AvailabilityZoneList: TypeAlias = list["aws_sdk_dax.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityZoneList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AvailabilityZoneList:
    return list(data)
