"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseCountingType``."""

from typing import Literal, TypeAlias, cast

LicenseCountingType: TypeAlias = Literal[
    "vCPU",
    "Instance",
    "Core",
    "Socket",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseCountingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseCountingType:
    return cast(LicenseCountingType, data)
