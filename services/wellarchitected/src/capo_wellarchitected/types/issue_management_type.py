"""Generated from Smithy shape ``com.amazonaws.wellarchitected#IssueManagementType``."""

from typing import Literal, TypeAlias, cast

IssueManagementType: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: IssueManagementType) -> str:
    return value


def deserialize_json(data: str) -> IssueManagementType:
    return cast(IssueManagementType, data)
