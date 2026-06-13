"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.column_metadata

ColumnList: TypeAlias = list[
    "aws_sdk_redshift_data.types.column_metadata.ColumnMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnList) -> list:
    import aws_sdk_redshift_data.types.column_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_data.types.column_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnList:
    import aws_sdk_redshift_data.types.column_metadata

    out: ColumnList = []
    for item in data:
        out.append(
            aws_sdk_redshift_data.types.column_metadata.deserialize_aws_json_1_1(item)
        )
    return out
