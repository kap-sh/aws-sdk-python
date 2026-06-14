"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

AssociationState: TypeAlias = Literal[
    "PENDING_INSTALL",
    "PENDING_INSTALL_DEPLOYMENT",
    "PENDING_UNINSTALL",
    "PENDING_UNINSTALL_DEPLOYMENT",
    "INSTALLING",
    "UNINSTALLING",
    "ERROR",
    "COMPLETED",
    "REMOVED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_INSTALL",
        "PENDING_INSTALL_DEPLOYMENT",
        "PENDING_UNINSTALL",
        "PENDING_UNINSTALL_DEPLOYMENT",
        "INSTALLING",
        "UNINSTALLING",
        "ERROR",
        "COMPLETED",
        "REMOVED",
    )
)


def serialize_aws_json_1_1(value: AssociationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationState value: {data!r}")
    return cast(AssociationState, data)
