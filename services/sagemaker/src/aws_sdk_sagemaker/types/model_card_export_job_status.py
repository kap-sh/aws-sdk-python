"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCardExportJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: ModelCardExportJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardExportJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCardExportJobStatus value: {data!r}")
    return cast(ModelCardExportJobStatus, data)
