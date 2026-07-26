"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseTableIncludeOrExcludeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_firehose.types.database_table_name

DatabaseTableIncludeOrExcludeList: TypeAlias = list[
    "capo_firehose.types.database_table_name.DatabaseTableName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseTableIncludeOrExcludeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DatabaseTableIncludeOrExcludeList:
    return list(data)
