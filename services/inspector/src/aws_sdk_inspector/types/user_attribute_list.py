"""Generated from Smithy shape ``com.amazonaws.inspector#UserAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.attribute

UserAttributeList: TypeAlias = list["aws_sdk_inspector.types.attribute.Attribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserAttributeList) -> list:
    import aws_sdk_inspector.types.attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector.types.attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UserAttributeList:
    import aws_sdk_inspector.types.attribute

    out: UserAttributeList = []
    for item in data:
        out.append(aws_sdk_inspector.types.attribute.deserialize_aws_json_1_1(item))
    return out
