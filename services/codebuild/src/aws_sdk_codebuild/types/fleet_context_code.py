"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetContextCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetContextCode: TypeAlias = Literal[
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "ACTION_REQUIRED",
    "PENDING_DELETION",
    "INSUFFICIENT_CAPACITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "ACTION_REQUIRED",
        "PENDING_DELETION",
        "INSUFFICIENT_CAPACITY",
    )
)


def serialize_aws_json_1_1(value: FleetContextCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetContextCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetContextCode value: {data!r}")
    return cast(FleetContextCode, data)
