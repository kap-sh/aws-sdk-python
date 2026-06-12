"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AccountJiraIssueManagementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

AccountJiraIssueManagementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AccountJiraIssueManagementStatus) -> str:
    return value


def deserialize_json(data: str) -> AccountJiraIssueManagementStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccountJiraIssueManagementStatus value: {data!r}"
        )
    return cast(AccountJiraIssueManagementStatus, data)
