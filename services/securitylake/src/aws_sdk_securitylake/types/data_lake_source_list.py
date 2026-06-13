"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_source

DataLakeSourceList: TypeAlias = list[
    "aws_sdk_securitylake.types.data_lake_source.DataLakeSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeSourceList) -> list:
    import aws_sdk_securitylake.types.data_lake_source

    out: list = []
    for item in value:
        out.append(aws_sdk_securitylake.types.data_lake_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeSourceList:
    import aws_sdk_securitylake.types.data_lake_source

    out: DataLakeSourceList = []
    for item in data:
        out.append(aws_sdk_securitylake.types.data_lake_source.deserialize_json(item))
    return out
