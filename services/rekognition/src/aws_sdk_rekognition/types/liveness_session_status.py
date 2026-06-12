"""Generated from Smithy shape ``com.amazonaws.rekognition#LivenessSessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

LivenessSessionStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "EXPIRED",
    )
)


def serialize_aws_json_1_1(value: LivenessSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LivenessSessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LivenessSessionStatus value: {data!r}")
    return cast(LivenessSessionStatus, data)
