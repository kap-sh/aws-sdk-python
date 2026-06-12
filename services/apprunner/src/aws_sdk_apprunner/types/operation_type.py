"""Generated from Smithy shape ``com.amazonaws.apprunner#OperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

OperationType: TypeAlias = Literal[
    "START_DEPLOYMENT",
    "CREATE_SERVICE",
    "PAUSE_SERVICE",
    "RESUME_SERVICE",
    "DELETE_SERVICE",
    "UPDATE_SERVICE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START_DEPLOYMENT",
        "CREATE_SERVICE",
        "PAUSE_SERVICE",
        "RESUME_SERVICE",
        "DELETE_SERVICE",
        "UPDATE_SERVICE",
    )
)


def serialize_aws_json_1_0(value: OperationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationType value: {data!r}")
    return cast(OperationType, data)
