"""Generated from Smithy shape ``com.amazonaws.ssm#ExecutionPreviewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ExecutionPreviewStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Success",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "InProgress",
        "Success",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: ExecutionPreviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionPreviewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionPreviewStatus value: {data!r}")
    return cast(ExecutionPreviewStatus, data)
