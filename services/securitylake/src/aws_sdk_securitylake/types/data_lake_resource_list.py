"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_resource

DataLakeResourceList: TypeAlias = list[
    "aws_sdk_securitylake.types.data_lake_resource.DataLakeResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeResourceList) -> list:
    import aws_sdk_securitylake.types.data_lake_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_securitylake.types.data_lake_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeResourceList:
    import aws_sdk_securitylake.types.data_lake_resource

    out: DataLakeResourceList = []
    for item in data:
        out.append(aws_sdk_securitylake.types.data_lake_resource.deserialize_json(item))
    return out
