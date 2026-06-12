"""Generated from Smithy shape ``com.amazonaws.dlm#PolicyTypeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

PolicyTypeValues: TypeAlias = Literal[
    "EBS_SNAPSHOT_MANAGEMENT",
    "IMAGE_MANAGEMENT",
    "EVENT_BASED_POLICY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EBS_SNAPSHOT_MANAGEMENT",
        "IMAGE_MANAGEMENT",
        "EVENT_BASED_POLICY",
    )
)


def serialize_json(value: PolicyTypeValues) -> str:
    return value


def deserialize_json(data: str) -> PolicyTypeValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyTypeValues value: {data!r}")
    return cast(PolicyTypeValues, data)
