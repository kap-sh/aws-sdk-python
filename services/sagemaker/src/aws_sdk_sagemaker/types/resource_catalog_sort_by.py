"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceCatalogSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ResourceCatalogSortBy: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreationTime",))


def serialize_aws_json_1_1(value: ResourceCatalogSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceCatalogSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceCatalogSortBy value: {data!r}")
    return cast(ResourceCatalogSortBy, data)
