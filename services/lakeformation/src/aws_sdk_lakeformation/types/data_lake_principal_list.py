"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataLakePrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.data_lake_principal

DataLakePrincipalList: TypeAlias = list[
    "aws_sdk_lakeformation.types.data_lake_principal.DataLakePrincipal"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakePrincipalList) -> list:
    import aws_sdk_lakeformation.types.data_lake_principal

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.data_lake_principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakePrincipalList:
    import aws_sdk_lakeformation.types.data_lake_principal

    out: DataLakePrincipalList = []
    for item in data:
        out.append(
            aws_sdk_lakeformation.types.data_lake_principal.deserialize_json(item)
        )
    return out
