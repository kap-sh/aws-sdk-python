"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.schema_version_error_item

SchemaVersionErrorList: TypeAlias = list[
    "capo_glue.types.schema_version_error_item.SchemaVersionErrorItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaVersionErrorList) -> list:
    import capo_glue.types.schema_version_error_item

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.schema_version_error_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SchemaVersionErrorList:
    import capo_glue.types.schema_version_error_item

    out: SchemaVersionErrorList = []
    for item in data:
        out.append(
            capo_glue.types.schema_version_error_item.deserialize_aws_json_1_1(item)
        )
    return out
