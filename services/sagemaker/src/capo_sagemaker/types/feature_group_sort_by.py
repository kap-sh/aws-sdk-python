"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroupSortBy``."""

from typing import Literal, TypeAlias, cast

FeatureGroupSortBy: TypeAlias = Literal[
    "Name",
    "FeatureGroupStatus",
    "OfflineStoreStatus",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureGroupSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureGroupSortBy:
    return cast(FeatureGroupSortBy, data)
