"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkforceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

WorkforceStatus: TypeAlias = Literal[
    "Initializing",
    "Updating",
    "Deleting",
    "Failed",
    "Active",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Initializing",
        "Updating",
        "Deleting",
        "Failed",
        "Active",
    )
)


def serialize_aws_json_1_1(value: WorkforceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkforceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkforceStatus value: {data!r}")
    return cast(WorkforceStatus, data)
