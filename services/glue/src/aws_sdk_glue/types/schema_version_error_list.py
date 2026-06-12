"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_version_error_item

SchemaVersionErrorList: TypeAlias = list[
    "aws_sdk_glue.types.schema_version_error_item.SchemaVersionErrorItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaVersionErrorList) -> list:
    import aws_sdk_glue.types.schema_version_error_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.schema_version_error_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SchemaVersionErrorList:
    import aws_sdk_glue.types.schema_version_error_item

    out: SchemaVersionErrorList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.schema_version_error_item.deserialize_aws_json_1_1(item)
        )
    return out
