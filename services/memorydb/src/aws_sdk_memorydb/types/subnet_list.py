"""Generated from Smithy shape ``com.amazonaws.memorydb#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.subnet

SubnetList: TypeAlias = list["aws_sdk_memorydb.types.subnet.Subnet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetList) -> list:
    import aws_sdk_memorydb.types.subnet

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.subnet.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubnetList:
    import aws_sdk_memorydb.types.subnet

    out: SubnetList = []
    for item in data:
        out.append(aws_sdk_memorydb.types.subnet.deserialize_aws_json_1_1(item))
    return out
