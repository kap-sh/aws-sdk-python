"""Generated from Smithy shape ``com.amazonaws.workmail#AccessEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

AccessEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_1(value: AccessEffect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessEffect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessEffect value: {data!r}")
    return cast(AccessEffect, data)
