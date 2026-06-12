"""Generated from Smithy shape ``com.amazonaws.athena#DataCatalogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

DataCatalogType: TypeAlias = Literal[
    "LAMBDA",
    "GLUE",
    "HIVE",
    "FEDERATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LAMBDA",
        "GLUE",
        "HIVE",
        "FEDERATED",
    )
)


def serialize_aws_json_1_1(value: DataCatalogType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataCatalogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataCatalogType value: {data!r}")
    return cast(DataCatalogType, data)
