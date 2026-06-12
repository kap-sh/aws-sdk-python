"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

LicenseConfigurationStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: LicenseConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LicenseConfigurationStatus value: {data!r}"
        )
    return cast(LicenseConfigurationStatus, data)
