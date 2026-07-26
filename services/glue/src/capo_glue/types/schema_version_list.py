"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.schema_version_list_item

SchemaVersionList: TypeAlias = list[
    "capo_glue.types.schema_version_list_item.SchemaVersionListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaVersionList) -> list:
    import capo_glue.types.schema_version_list_item

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.schema_version_list_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SchemaVersionList:
    import capo_glue.types.schema_version_list_item

    out: SchemaVersionList = []
    for item in data:
        out.append(
            capo_glue.types.schema_version_list_item.deserialize_aws_json_1_1(item)
        )
    return out
