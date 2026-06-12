"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InferenceComponentStatus: TypeAlias = Literal[
    "InService",
    "Creating",
    "Updating",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InService",
        "Creating",
        "Updating",
        "Failed",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: InferenceComponentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceComponentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceComponentStatus value: {data!r}")
    return cast(InferenceComponentStatus, data)
