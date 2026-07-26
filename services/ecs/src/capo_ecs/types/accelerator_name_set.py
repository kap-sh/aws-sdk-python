"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorNameSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.accelerator_name

AcceleratorNameSet: TypeAlias = list["capo_ecs.types.accelerator_name.AcceleratorName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorNameSet) -> list:
    import capo_ecs.types.accelerator_name

    out: list = []
    for item in value:
        out.append(capo_ecs.types.accelerator_name.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AcceleratorNameSet:
    import capo_ecs.types.accelerator_name

    out: AcceleratorNameSet = []
    for item in data:
        out.append(capo_ecs.types.accelerator_name.deserialize_aws_json_1_1(item))
    return out
