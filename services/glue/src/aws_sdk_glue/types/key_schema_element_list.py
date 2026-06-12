"""Generated from Smithy shape ``com.amazonaws.glue#KeySchemaElementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.key_schema_element

KeySchemaElementList: TypeAlias = list[
    "aws_sdk_glue.types.key_schema_element.KeySchemaElement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeySchemaElementList) -> list:
    import aws_sdk_glue.types.key_schema_element

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.key_schema_element.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeySchemaElementList:
    import aws_sdk_glue.types.key_schema_element

    out: KeySchemaElementList = []
    for item in data:
        out.append(aws_sdk_glue.types.key_schema_element.deserialize_aws_json_1_1(item))
    return out
