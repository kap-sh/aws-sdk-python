"""Generated from Smithy shape ``com.amazonaws.redshiftdata#DbGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.string

DbGroupList: TypeAlias = list["aws_sdk_redshift_data.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DbGroupList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DbGroupList:
    return list(data)
