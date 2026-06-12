"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroupSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FeatureGroupSortBy: TypeAlias = Literal[
    "Name",
    "FeatureGroupStatus",
    "OfflineStoreStatus",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "FeatureGroupStatus",
        "OfflineStoreStatus",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: FeatureGroupSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureGroupSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureGroupSortBy value: {data!r}")
    return cast(FeatureGroupSortBy, data)
