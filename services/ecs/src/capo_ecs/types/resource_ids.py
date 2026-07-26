"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.string

ResourceIds: TypeAlias = list["capo_ecs.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceIds:
    return list(data)
