"""Generated from Smithy shape ``com.amazonaws.organizations#ChildType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

ChildType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATIONAL_UNIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "ORGANIZATIONAL_UNIT",
    )
)


def serialize_aws_json_1_1(value: ChildType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChildType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChildType value: {data!r}")
    return cast(ChildType, data)
