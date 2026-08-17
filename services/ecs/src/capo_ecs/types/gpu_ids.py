"""Generated from Smithy shape ``com.amazonaws.ecs#GpuIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.string

GpuIds: TypeAlias = list["capo_ecs.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GpuIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> GpuIds:
    return [item for item in data if item is not None]
