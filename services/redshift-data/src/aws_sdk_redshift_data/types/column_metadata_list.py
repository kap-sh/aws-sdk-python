"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ColumnMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.column_metadata

ColumnMetadataList: TypeAlias = list[
    "aws_sdk_redshift_data.types.column_metadata.ColumnMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnMetadataList) -> list:
    import aws_sdk_redshift_data.types.column_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_data.types.column_metadata.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnMetadataList:
    import aws_sdk_redshift_data.types.column_metadata

    out: ColumnMetadataList = []
    for item in data:
        out.append(
            aws_sdk_redshift_data.types.column_metadata.deserialize_aws_json_1_1(item)
        )
    return out
