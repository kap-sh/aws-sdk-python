"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ExperienceStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ExperienceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExperienceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExperienceStatus value: {data!r}")
    return cast(ExperienceStatus, data)
