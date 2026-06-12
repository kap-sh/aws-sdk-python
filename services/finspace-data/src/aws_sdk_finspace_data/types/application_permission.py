"""Generated from Smithy shape ``com.amazonaws.finspacedata#ApplicationPermission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CreateDataset",
        "ManageClusters",
        "ManageUsersAndGroups",
        "ManageAttributeSets",
        "ViewAuditData",
        "AccessNotebooks",
        "GetTemporaryCredentials",
    )
)


def serialize_json(value: ApplicationPermission) -> str:
    return value


def deserialize_json(data: str) -> ApplicationPermission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationPermission value: {data!r}")
    return cast(ApplicationPermission, data)
