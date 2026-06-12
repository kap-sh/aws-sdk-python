"""Generated from Smithy shape ``com.amazonaws.glue#TableAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.table_attributes

TableAttributesList: TypeAlias = list[
    "aws_sdk_glue.types.table_attributes.TableAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableAttributesList) -> list:
    import aws_sdk_glue.types.table_attributes

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.table_attributes.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableAttributesList:
    import aws_sdk_glue.types.table_attributes

    out: TableAttributesList = []
    for item in data:
        out.append(aws_sdk_glue.types.table_attributes.deserialize_aws_json_1_1(item))
    return out
