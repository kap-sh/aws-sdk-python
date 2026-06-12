"""Generated from Smithy shape ``com.amazonaws.organizations#TargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

TargetType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATIONAL_UNIT",
    "ROOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "ORGANIZATIONAL_UNIT",
        "ROOT",
    )
)


def serialize_aws_json_1_1(value: TargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetType value: {data!r}")
    return cast(TargetType, data)
