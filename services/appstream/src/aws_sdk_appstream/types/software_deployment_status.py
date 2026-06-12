"""Generated from Smithy shape ``com.amazonaws.appstream#SoftwareDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

SoftwareDeploymentStatus: TypeAlias = Literal[
    "STAGED_FOR_INSTALLATION",
    "PENDING_INSTALLATION",
    "INSTALLED",
    "STAGED_FOR_UNINSTALLATION",
    "PENDING_UNINSTALLATION",
    "FAILED_TO_INSTALL",
    "FAILED_TO_UNINSTALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STAGED_FOR_INSTALLATION",
        "PENDING_INSTALLATION",
        "INSTALLED",
        "STAGED_FOR_UNINSTALLATION",
        "PENDING_UNINSTALLATION",
        "FAILED_TO_INSTALL",
        "FAILED_TO_UNINSTALL",
    )
)


def serialize_aws_json_1_1(value: SoftwareDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SoftwareDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SoftwareDeploymentStatus value: {data!r}")
    return cast(SoftwareDeploymentStatus, data)
