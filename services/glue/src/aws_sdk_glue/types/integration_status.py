"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

IntegrationStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "MODIFYING",
    "FAILED",
    "DELETING",
    "SYNCING",
    "NEEDS_ATTENTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "MODIFYING",
        "FAILED",
        "DELETING",
        "SYNCING",
        "NEEDS_ATTENTION",
    )
)


def serialize_aws_json_1_1(value: IntegrationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IntegrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationStatus value: {data!r}")
    return cast(IntegrationStatus, data)
