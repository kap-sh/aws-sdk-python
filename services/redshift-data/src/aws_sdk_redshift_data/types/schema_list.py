"""Generated from Smithy shape ``com.amazonaws.redshiftdata#SchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.string

SchemaList: TypeAlias = list["aws_sdk_redshift_data.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SchemaList:
    return list(data)
