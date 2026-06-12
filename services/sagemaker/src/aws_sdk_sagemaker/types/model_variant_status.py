"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelVariantStatus: TypeAlias = Literal[
    "Creating",
    "Updating",
    "InService",
    "Deleting",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Updating",
        "InService",
        "Deleting",
        "Deleted",
    )
)


def serialize_aws_json_1_1(value: ModelVariantStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelVariantStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelVariantStatus value: {data!r}")
    return cast(ModelVariantStatus, data)
