"""Generated from Smithy shape ``com.amazonaws.emr#XmlStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string

XmlStringList: TypeAlias = list["aws_sdk_emr.types.xml_string.XmlString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XmlStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> XmlStringList:
    return list(data)
