"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WorkloadIssueManagementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

WorkloadIssueManagementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "INHERIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "INHERIT",
    )
)


def serialize_json(value: WorkloadIssueManagementStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkloadIssueManagementStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkloadIssueManagementStatus value: {data!r}"
        )
    return cast(WorkloadIssueManagementStatus, data)
