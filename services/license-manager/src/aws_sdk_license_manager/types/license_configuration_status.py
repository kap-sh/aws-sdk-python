"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

LicenseConfigurationStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseConfigurationStatus:
    return cast(LicenseConfigurationStatus, data)
