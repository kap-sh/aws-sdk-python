"""Generated from Smithy shape ``com.amazonaws.ecr#ScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ScanType: TypeAlias = Literal[
    "BASIC",
    "ENHANCED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "ENHANCED",
    )
)


def serialize_aws_json_1_1(value: ScanType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanType value: {data!r}")
    return cast(ScanType, data)
