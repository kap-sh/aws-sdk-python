"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConversionTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

LicenseConversionTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: LicenseConversionTaskStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseConversionTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LicenseConversionTaskStatus value: {data!r}"
        )
    return cast(LicenseConversionTaskStatus, data)
