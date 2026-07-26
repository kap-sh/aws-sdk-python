"""Generated from Smithy shape ``com.amazonaws.athena#DataCatalogType``."""

from typing import Literal, TypeAlias, cast

DataCatalogType: TypeAlias = Literal[
    "LAMBDA",
    "GLUE",
    "HIVE",
    "FEDERATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCatalogType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataCatalogType:
    return cast(DataCatalogType, data)
