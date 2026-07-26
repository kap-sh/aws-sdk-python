"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceCatalogSortBy``."""

from typing import Literal, TypeAlias, cast

ResourceCatalogSortBy: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCatalogSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceCatalogSortBy:
    return cast(ResourceCatalogSortBy, data)
