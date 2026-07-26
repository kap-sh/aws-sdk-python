"""Generated from Smithy shape ``com.amazonaws.glue#ColumnImportanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.column_importance

ColumnImportanceList: TypeAlias = list[
    "capo_glue.types.column_importance.ColumnImportance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnImportanceList) -> list:
    import capo_glue.types.column_importance

    out: list = []
    for item in value:
        out.append(capo_glue.types.column_importance.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnImportanceList:
    import capo_glue.types.column_importance

    out: ColumnImportanceList = []
    for item in data:
        out.append(capo_glue.types.column_importance.deserialize_aws_json_1_1(item))
    return out
