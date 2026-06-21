"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseEdition``."""

from typing import Literal, TypeAlias, cast

LicenseEdition: TypeAlias = Literal[
    "Enterprise",
    "Standard",
    "Free",
    "NoLicenseEditionFound",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseEdition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseEdition:
    return cast(LicenseEdition, data)
