"""Generated from Smithy shape ``com.amazonaws.inspector#AttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.attribute

AttributeList: TypeAlias = list["aws_sdk_inspector.types.attribute.Attribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeList) -> list:
    import aws_sdk_inspector.types.attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector.types.attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttributeList:
    import aws_sdk_inspector.types.attribute

    out: AttributeList = []
    for item in data:
        out.append(aws_sdk_inspector.types.attribute.deserialize_aws_json_1_1(item))
    return out
