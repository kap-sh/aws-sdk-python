"""Generated from Smithy shape ``com.amazonaws.glue#AuditColumnNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.column_name_string

AuditColumnNamesList: TypeAlias = list[
    "capo_glue.types.column_name_string.ColumnNameString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuditColumnNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AuditColumnNamesList:
    return list(data)
