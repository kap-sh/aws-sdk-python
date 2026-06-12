"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FeatureGroupStatus: TypeAlias = Literal[
    "Creating",
    "Created",
    "CreateFailed",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Created",
        "CreateFailed",
        "Deleting",
        "DeleteFailed",
    )
)


def serialize_aws_json_1_1(value: FeatureGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureGroupStatus value: {data!r}")
    return cast(FeatureGroupStatus, data)
