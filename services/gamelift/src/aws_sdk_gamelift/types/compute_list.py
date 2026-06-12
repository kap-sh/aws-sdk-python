"""Generated from Smithy shape ``com.amazonaws.gamelift#ComputeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.compute

ComputeList: TypeAlias = list["aws_sdk_gamelift.types.compute.Compute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeList) -> list:
    import aws_sdk_gamelift.types.compute

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.compute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComputeList:
    import aws_sdk_gamelift.types.compute

    out: ComputeList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.compute.deserialize_aws_json_1_1(item))
    return out
