"""Generated from Smithy shape ``com.amazonaws.cloud9#ManagedCredentialsStatus``."""

from typing import Literal, TypeAlias, cast

ManagedCredentialsStatus: TypeAlias = Literal[
    "ENABLED_ON_CREATE",
    "ENABLED_BY_OWNER",
    "DISABLED_BY_DEFAULT",
    "DISABLED_BY_OWNER",
    "DISABLED_BY_COLLABORATOR",
    "PENDING_REMOVAL_BY_COLLABORATOR",
    "PENDING_START_REMOVAL_BY_COLLABORATOR",
    "PENDING_REMOVAL_BY_OWNER",
    "PENDING_START_REMOVAL_BY_OWNER",
    "FAILED_REMOVAL_BY_COLLABORATOR",
    "FAILED_REMOVAL_BY_OWNER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedCredentialsStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedCredentialsStatus:
    return cast(ManagedCredentialsStatus, data)
