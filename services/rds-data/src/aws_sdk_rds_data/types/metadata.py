"""Generated from Smithy shape ``com.amazonaws.rdsdata#Metadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.column_metadata

Metadata: TypeAlias = list["aws_sdk_rds_data.types.column_metadata.ColumnMetadata"]


# --- restJson1 ser/de ---
def serialize_json(value: Metadata) -> list:
    import aws_sdk_rds_data.types.column_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_rds_data.types.column_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> Metadata:
    import aws_sdk_rds_data.types.column_metadata

    out: Metadata = []
    for item in data:
        out.append(aws_sdk_rds_data.types.column_metadata.deserialize_json(item))
    return out
