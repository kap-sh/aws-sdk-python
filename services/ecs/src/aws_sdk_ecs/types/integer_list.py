"""Generated from Smithy shape ``com.amazonaws.ecs#IntegerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer

IntegerList: TypeAlias = list["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IntegerList:
    return list(data)
