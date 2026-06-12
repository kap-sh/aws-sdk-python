"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCardStatus: TypeAlias = Literal[
    "Draft",
    "PendingReview",
    "Approved",
    "Archived",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Draft",
        "PendingReview",
        "Approved",
        "Archived",
    )
)


def serialize_aws_json_1_1(value: ModelCardStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCardStatus value: {data!r}")
    return cast(ModelCardStatus, data)
