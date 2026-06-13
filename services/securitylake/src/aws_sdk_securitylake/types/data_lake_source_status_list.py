"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeSourceStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_source_status

DataLakeSourceStatusList: TypeAlias = list[
    "aws_sdk_securitylake.types.data_lake_source_status.DataLakeSourceStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeSourceStatusList) -> list:
    import aws_sdk_securitylake.types.data_lake_source_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securitylake.types.data_lake_source_status.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataLakeSourceStatusList:
    import aws_sdk_securitylake.types.data_lake_source_status

    out: DataLakeSourceStatusList = []
    for item in data:
        out.append(
            aws_sdk_securitylake.types.data_lake_source_status.deserialize_json(item)
        )
    return out
