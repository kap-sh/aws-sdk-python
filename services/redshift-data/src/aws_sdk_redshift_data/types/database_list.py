"""Generated from Smithy shape ``com.amazonaws.redshiftdata#DatabaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.string

DatabaseList: TypeAlias = list["aws_sdk_redshift_data.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DatabaseList:
    return list(data)
