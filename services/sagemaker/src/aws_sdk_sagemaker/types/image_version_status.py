"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ImageVersionStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "CREATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "CREATE_FAILED",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_aws_json_1_1(value: ImageVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageVersionStatus value: {data!r}")
    return cast(ImageVersionStatus, data)
