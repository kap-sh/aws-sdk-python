"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.accelerator_type

AcceleratorTypeSet: TypeAlias = list[
    "aws_sdk_ecs.types.accelerator_type.AcceleratorType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorTypeSet) -> list:
    import aws_sdk_ecs.types.accelerator_type

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.accelerator_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AcceleratorTypeSet:
    import aws_sdk_ecs.types.accelerator_type

    out: AcceleratorTypeSet = []
    for item in data:
        out.append(aws_sdk_ecs.types.accelerator_type.deserialize_aws_json_1_1(item))
    return out
