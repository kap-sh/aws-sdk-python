"""Generated from Smithy shape ``com.amazonaws.ecs#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attribute

Attributes: TypeAlias = list["aws_sdk_ecs.types.attribute.Attribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attributes) -> list:
    import aws_sdk_ecs.types.attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Attributes:
    import aws_sdk_ecs.types.attribute

    out: Attributes = []
    for item in data:
        out.append(aws_sdk_ecs.types.attribute.deserialize_aws_json_1_1(item))
    return out
