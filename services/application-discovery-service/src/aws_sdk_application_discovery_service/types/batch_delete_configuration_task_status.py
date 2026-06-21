"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#BatchDeleteConfigurationTaskStatus``."""

from typing import Literal, TypeAlias, cast

BatchDeleteConfigurationTaskStatus: TypeAlias = Literal[
    "INITIALIZING",
    "VALIDATING",
    "DELETING",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteConfigurationTaskStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchDeleteConfigurationTaskStatus:
    return cast(BatchDeleteConfigurationTaskStatus, data)
