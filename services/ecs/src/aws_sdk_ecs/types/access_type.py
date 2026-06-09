"""Generated from Smithy shape ``com.amazonaws.ecs#AccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

AccessType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "PRIVATE",
    )
)


def serialize_aws_json_1_1(value: AccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessType value: {data!r}")
    return cast(AccessType, data)
