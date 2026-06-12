"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

LicenseStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING_AVAILABLE",
    "DEACTIVATED",
    "SUSPENDED",
    "EXPIRED",
    "PENDING_DELETE",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING_AVAILABLE",
        "DEACTIVATED",
        "SUSPENDED",
        "EXPIRED",
        "PENDING_DELETE",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: LicenseStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseStatus value: {data!r}")
    return cast(LicenseStatus, data)
