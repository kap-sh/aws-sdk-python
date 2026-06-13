"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeNamespaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_namespace

DataLakeNamespaceList: TypeAlias = list[
    "aws_sdk_supplychain.types.data_lake_namespace.DataLakeNamespace"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeNamespaceList) -> list:
    import aws_sdk_supplychain.types.data_lake_namespace

    out: list = []
    for item in value:
        out.append(aws_sdk_supplychain.types.data_lake_namespace.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLakeNamespaceList:
    import aws_sdk_supplychain.types.data_lake_namespace

    out: DataLakeNamespaceList = []
    for item in data:
        out.append(aws_sdk_supplychain.types.data_lake_namespace.deserialize_json(item))
    return out
