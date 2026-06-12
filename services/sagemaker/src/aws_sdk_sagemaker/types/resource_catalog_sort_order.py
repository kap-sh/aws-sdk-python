"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceCatalogSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ResourceCatalogSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ascending",
        "Descending",
    )
)


def serialize_aws_json_1_1(value: ResourceCatalogSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceCatalogSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceCatalogSortOrder value: {data!r}")
    return cast(ResourceCatalogSortOrder, data)
