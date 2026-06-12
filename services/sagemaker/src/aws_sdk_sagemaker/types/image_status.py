"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ImageStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "CREATE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_aws_json_1_1(value: ImageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageStatus value: {data!r}")
    return cast(ImageStatus, data)
