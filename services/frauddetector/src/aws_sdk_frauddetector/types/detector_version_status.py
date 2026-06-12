"""Generated from Smithy shape ``com.amazonaws.frauddetector#DetectorVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

DetectorVersionStatus: TypeAlias = Literal[
    "DRAFT",
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: DetectorVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetectorVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetectorVersionStatus value: {data!r}")
    return cast(DetectorVersionStatus, data)
