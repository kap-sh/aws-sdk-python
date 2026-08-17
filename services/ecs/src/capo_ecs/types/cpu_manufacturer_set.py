"""Generated from Smithy shape ``com.amazonaws.ecs#CpuManufacturerSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.cpu_manufacturer

CpuManufacturerSet: TypeAlias = list["capo_ecs.types.cpu_manufacturer.CpuManufacturer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CpuManufacturerSet) -> list:
    import capo_ecs.types.cpu_manufacturer

    out: list = []
    for item in value:
        out.append(capo_ecs.types.cpu_manufacturer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CpuManufacturerSet:
    import capo_ecs.types.cpu_manufacturer

    out: CpuManufacturerSet = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.cpu_manufacturer.deserialize_aws_json_1_1(item))
    return out
