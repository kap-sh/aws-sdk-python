"""Generated from Smithy shape ``com.amazonaws.workmail#IpRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.ip_range

IpRangeList: TypeAlias = list["aws_sdk_workmail.types.ip_range.IpRange"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRangeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpRangeList:
    return list(data)
