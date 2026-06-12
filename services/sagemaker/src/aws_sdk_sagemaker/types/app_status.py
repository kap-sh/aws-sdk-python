"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AppStatus: TypeAlias = Literal[
    "Deleted",
    "Deleting",
    "Failed",
    "InService",
    "Pending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Deleted",
        "Deleting",
        "Failed",
        "InService",
        "Pending",
    )
)


def serialize_aws_json_1_1(value: AppStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppStatus value: {data!r}")
    return cast(AppStatus, data)
