"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

FleetStatusCode: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ROTATING",
    "PENDING_DELETION",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_ROLLBACK_FAILED",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "ROTATING",
        "PENDING_DELETION",
        "DELETING",
        "CREATE_FAILED",
        "UPDATE_ROLLBACK_FAILED",
        "ACTIVE",
    )
)


def serialize_aws_json_1_1(value: FleetStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FleetStatusCode value: {data!r}")
    return cast(FleetStatusCode, data)
