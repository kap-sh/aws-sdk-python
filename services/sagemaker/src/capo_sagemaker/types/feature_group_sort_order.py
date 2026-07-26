"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroupSortOrder``."""

from typing import Literal, TypeAlias, cast

FeatureGroupSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureGroupSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureGroupSortOrder:
    return cast(FeatureGroupSortOrder, data)
