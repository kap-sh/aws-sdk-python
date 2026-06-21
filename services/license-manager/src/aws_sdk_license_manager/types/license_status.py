"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: LicenseStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseStatus:
    return cast(LicenseStatus, data)
