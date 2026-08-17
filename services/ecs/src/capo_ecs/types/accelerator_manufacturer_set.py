"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorManufacturerSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.accelerator_manufacturer

AcceleratorManufacturerSet: TypeAlias = list[
    "capo_ecs.types.accelerator_manufacturer.AcceleratorManufacturer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorManufacturerSet) -> list:
    import capo_ecs.types.accelerator_manufacturer

    out: list = []
    for item in value:
        out.append(capo_ecs.types.accelerator_manufacturer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AcceleratorManufacturerSet:
    import capo_ecs.types.accelerator_manufacturer

    out: AcceleratorManufacturerSet = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.accelerator_manufacturer.deserialize_aws_json_1_1(item)
        )
    return out
