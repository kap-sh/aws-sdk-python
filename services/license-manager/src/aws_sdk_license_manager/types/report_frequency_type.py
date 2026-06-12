"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportFrequencyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

ReportFrequencyType: TypeAlias = Literal[
    "DAY",
    "WEEK",
    "MONTH",
    "ONE_TIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAY",
        "WEEK",
        "MONTH",
        "ONE_TIME",
    )
)


def serialize_aws_json_1_1(value: ReportFrequencyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportFrequencyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReportFrequencyType value: {data!r}")
    return cast(ReportFrequencyType, data)
