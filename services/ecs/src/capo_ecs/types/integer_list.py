"""Generated from Smithy shape ``com.amazonaws.ecs#IntegerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer

IntegerList: TypeAlias = list["capo_ecs.types.boxed_integer.BoxedInteger"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IntegerList:
    return [item for item in data if item is not None]
