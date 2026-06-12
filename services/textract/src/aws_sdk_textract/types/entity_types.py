"""Generated from Smithy shape ``com.amazonaws.textract#EntityTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.entity_type

EntityTypes: TypeAlias = list["aws_sdk_textract.types.entity_type.EntityType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityTypes) -> list:
    import aws_sdk_textract.types.entity_type

    out: list = []
    for item in value:
        out.append(aws_sdk_textract.types.entity_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntityTypes:
    import aws_sdk_textract.types.entity_type

    out: EntityTypes = []
    for item in data:
        out.append(aws_sdk_textract.types.entity_type.deserialize_aws_json_1_1(item))
    return out
