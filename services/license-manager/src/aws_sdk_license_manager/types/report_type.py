"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

ReportType: TypeAlias = Literal[
    "LicenseConfigurationSummaryReport",
    "LicenseConfigurationUsageReport",
    "LicenseAssetGroupUsageReport",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LicenseConfigurationSummaryReport",
        "LicenseConfigurationUsageReport",
        "LicenseAssetGroupUsageReport",
    )
)


def serialize_aws_json_1_1(value: ReportType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportType value: {data!r}")
    return cast(ReportType, data)
