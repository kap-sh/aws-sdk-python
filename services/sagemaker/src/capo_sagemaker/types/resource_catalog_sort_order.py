"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceCatalogSortOrder``."""

from typing import Literal, TypeAlias, cast

ResourceCatalogSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCatalogSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceCatalogSortOrder:
    return cast(ResourceCatalogSortOrder, data)
