"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.accelerator_type

AcceleratorTypeSet: TypeAlias = list["capo_ecs.types.accelerator_type.AcceleratorType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorTypeSet) -> list:
    import capo_ecs.types.accelerator_type

    out: list = []
    for item in value:
        out.append(capo_ecs.types.accelerator_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AcceleratorTypeSet:
    import capo_ecs.types.accelerator_type

    out: AcceleratorTypeSet = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.accelerator_type.deserialize_aws_json_1_1(item))
    return out
