"""Generated from Smithy shape ``com.amazonaws.ssm#AccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AccessType: TypeAlias = Literal[
    "Standard",
    "JustInTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "JustInTime",
    )
)


def serialize_aws_json_1_1(value: AccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessType value: {data!r}")
    return cast(AccessType, data)
