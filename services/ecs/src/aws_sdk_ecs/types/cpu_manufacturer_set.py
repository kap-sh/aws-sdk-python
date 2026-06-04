"""Generated from Smithy shape ``com.amazonaws.ecs#CpuManufacturerSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cpu_manufacturer

CpuManufacturerSet: TypeAlias = list[
    "aws_sdk_ecs.types.cpu_manufacturer.CpuManufacturer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CpuManufacturerSet) -> list:
    import aws_sdk_ecs.types.cpu_manufacturer

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.cpu_manufacturer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CpuManufacturerSet:
    import aws_sdk_ecs.types.cpu_manufacturer

    out: CpuManufacturerSet = []
    for item in data:
        out.append(aws_sdk_ecs.types.cpu_manufacturer.deserialize_aws_json_1_1(item))
    return out
