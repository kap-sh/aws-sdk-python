"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConversionTaskStatus``."""

from typing import Literal, TypeAlias, cast

LicenseConversionTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConversionTaskStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseConversionTaskStatus:
    return cast(LicenseConversionTaskStatus, data)
