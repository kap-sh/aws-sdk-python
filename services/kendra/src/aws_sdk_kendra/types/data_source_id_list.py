"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_id

DataSourceIdList: TypeAlias = list["aws_sdk_kendra.types.data_source_id.DataSourceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataSourceIdList:
    return list(data)
