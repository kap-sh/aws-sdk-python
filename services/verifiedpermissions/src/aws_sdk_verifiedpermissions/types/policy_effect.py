"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

PolicyEffect: TypeAlias = Literal[
    "Permit",
    "Forbid",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Permit",
        "Forbid",
    )
)


def serialize_aws_json_1_0(value: PolicyEffect) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PolicyEffect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyEffect value: {data!r}")
    return cast(PolicyEffect, data)
