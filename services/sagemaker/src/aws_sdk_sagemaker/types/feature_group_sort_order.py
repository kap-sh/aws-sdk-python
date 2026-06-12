"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroupSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FeatureGroupSortOrder: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: FeatureGroupSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureGroupSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureGroupSortOrder value: {data!r}")
    return cast(FeatureGroupSortOrder, data)
