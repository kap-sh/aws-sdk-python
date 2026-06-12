"""Generated from Smithy shape ``com.amazonaws.apprunner#OperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

OperationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_FAILED",
    "ROLLBACK_SUCCEEDED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
        "ROLLBACK_IN_PROGRESS",
        "ROLLBACK_FAILED",
        "ROLLBACK_SUCCEEDED",
    )
)


def serialize_aws_json_1_0(value: OperationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationStatus value: {data!r}")
    return cast(OperationStatus, data)
