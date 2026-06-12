"""Generated from Smithy shape ``com.amazonaws.organizations#ParentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

ParentType: TypeAlias = Literal[
    "ROOT",
    "ORGANIZATIONAL_UNIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROOT",
        "ORGANIZATIONAL_UNIT",
    )
)


def serialize_aws_json_1_1(value: ParentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParentType value: {data!r}")
    return cast(ParentType, data)
