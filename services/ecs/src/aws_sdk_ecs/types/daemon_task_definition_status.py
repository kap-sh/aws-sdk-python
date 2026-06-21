"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

DaemonTaskDefinitionStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETE_IN_PROGRESS",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonTaskDefinitionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonTaskDefinitionStatus:
    return cast(DaemonTaskDefinitionStatus, data)
