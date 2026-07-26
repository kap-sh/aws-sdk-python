"""Generated from Smithy shape ``com.amazonaws.glue#SelectedFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.entity_field_name

SelectedFields: TypeAlias = list["capo_glue.types.entity_field_name.EntityFieldName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectedFields) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SelectedFields:
    return list(data)
