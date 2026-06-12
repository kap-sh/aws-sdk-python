"""Generated from Smithy shape ``com.amazonaws.personalize#ObjectiveSensitivity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

ObjectiveSensitivity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "OFF",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
        "OFF",
    )
)


def serialize_aws_json_1_1(value: ObjectiveSensitivity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectiveSensitivity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObjectiveSensitivity value: {data!r}")
    return cast(ObjectiveSensitivity, data)
