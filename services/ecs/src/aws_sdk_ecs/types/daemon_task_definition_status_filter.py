"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionStatusFilter``."""

from typing import Literal, TypeAlias, cast

DaemonTaskDefinitionStatusFilter: TypeAlias = Literal[
    "ACTIVE",
    "DELETE_IN_PROGRESS",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonTaskDefinitionStatusFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonTaskDefinitionStatusFilter:
    return cast(DaemonTaskDefinitionStatusFilter, data)
