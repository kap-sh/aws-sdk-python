"""Generated from Smithy shape ``com.amazonaws.ecs#ExcludedInstanceTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.excluded_instance_type

ExcludedInstanceTypeSet: TypeAlias = list[
    "capo_ecs.types.excluded_instance_type.ExcludedInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludedInstanceTypeSet) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludedInstanceTypeSet:
    return [item for item in data if item is not None]
