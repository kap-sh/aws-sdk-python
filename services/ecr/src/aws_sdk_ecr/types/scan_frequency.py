"""Generated from Smithy shape ``com.amazonaws.ecr#ScanFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ScanFrequency: TypeAlias = Literal[
    "SCAN_ON_PUSH",
    "CONTINUOUS_SCAN",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCAN_ON_PUSH",
        "CONTINUOUS_SCAN",
        "MANUAL",
    )
)


def serialize_aws_json_1_1(value: ScanFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanFrequency value: {data!r}")
    return cast(ScanFrequency, data)
