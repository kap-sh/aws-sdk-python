"""Generated from Smithy shape ``com.amazonaws.finspacedata#ApplicationPermission``."""

from typing import Literal, TypeAlias, cast

ApplicationPermission: TypeAlias = Literal[
    "CreateDataset",
    "ManageClusters",
    "ManageUsersAndGroups",
    "ManageAttributeSets",
    "ViewAuditData",
    "AccessNotebooks",
    "GetTemporaryCredentials",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPermission) -> str:
    return value


def deserialize_json(data: str) -> ApplicationPermission:
    return cast(ApplicationPermission, data)
