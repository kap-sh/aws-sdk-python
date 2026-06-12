"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteConfigurationTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

BatchDeleteConfigurationTaskStatus: TypeAlias = Literal[
    "INITIALIZING",
    "VALIDATING",
    "DELETING",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZING",
        "VALIDATING",
        "DELETING",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: BatchDeleteConfigurationTaskStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchDeleteConfigurationTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchDeleteConfigurationTaskStatus value: {data!r}"
        )
    return cast(BatchDeleteConfigurationTaskStatus, data)
