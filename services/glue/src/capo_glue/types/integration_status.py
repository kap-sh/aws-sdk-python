"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: IntegrationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IntegrationStatus:
    return cast(IntegrationStatus, data)
