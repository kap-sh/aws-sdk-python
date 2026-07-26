"""Generated from Smithy shape ``com.amazonaws.glue#SchemaListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.schema_list_item

SchemaListDefinition: TypeAlias = list[
    "capo_glue.types.schema_list_item.SchemaListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaListDefinition) -> list:
    import capo_glue.types.schema_list_item

    out: list = []
    for item in value:
        out.append(capo_glue.types.schema_list_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SchemaListDefinition:
    import capo_glue.types.schema_list_item

    out: SchemaListDefinition = []
    for item in data:
        out.append(capo_glue.types.schema_list_item.deserialize_aws_json_1_1(item))
    return out
