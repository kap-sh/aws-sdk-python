"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AccountJiraIssueManagementStatus``."""

from typing import Literal, TypeAlias, cast

AccountJiraIssueManagementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountJiraIssueManagementStatus) -> str:
    return value


def deserialize_json(data: str) -> AccountJiraIssueManagementStatus:
    return cast(AccountJiraIssueManagementStatus, data)
