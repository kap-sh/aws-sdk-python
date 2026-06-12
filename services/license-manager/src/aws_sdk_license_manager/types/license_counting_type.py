"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseCountingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

LicenseCountingType: TypeAlias = Literal[
    "vCPU",
    "Instance",
    "Core",
    "Socket",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "vCPU",
        "Instance",
        "Core",
        "Socket",
    )
)


def serialize_aws_json_1_1(value: LicenseCountingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseCountingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseCountingType value: {data!r}")
    return cast(LicenseCountingType, data)
