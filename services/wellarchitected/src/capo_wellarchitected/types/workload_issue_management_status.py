"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadIssueManagementStatus``."""

from typing import Literal, TypeAlias, cast

WorkloadIssueManagementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "INHERIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadIssueManagementStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkloadIssueManagementStatus:
    return cast(WorkloadIssueManagementStatus, data)
