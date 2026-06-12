"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseColumnIncludeOrExcludeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.database_column_name

DatabaseColumnIncludeOrExcludeList: TypeAlias = list[
    "aws_sdk_firehose.types.database_column_name.DatabaseColumnName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseColumnIncludeOrExcludeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DatabaseColumnIncludeOrExcludeList:
    return list(data)
