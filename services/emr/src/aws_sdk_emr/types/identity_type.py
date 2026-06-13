"""Generated from Smithy shape ``com.amazonaws.emr#IdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

IdentityType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "GROUP",
    )
)


def serialize_aws_json_1_1(value: IdentityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityType value: {data!r}")
    return cast(IdentityType, data)
