"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeExceptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_exception

DataLakeExceptionList: TypeAlias = list[
    "aws_sdk_securitylake.types.data_lake_exception.DataLakeException"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeExceptionList) -> list:
    import aws_sdk_securitylake.types.data_lake_exception

    out: list = []
    for item in value:
        out.append(aws_sdk_securitylake.types.data_lake_exception.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeExceptionList:
    import aws_sdk_securitylake.types.data_lake_exception

    out: DataLakeExceptionList = []
    for item in data:
        out.append(
            aws_sdk_securitylake.types.data_lake_exception.deserialize_json(item)
        )
    return out
