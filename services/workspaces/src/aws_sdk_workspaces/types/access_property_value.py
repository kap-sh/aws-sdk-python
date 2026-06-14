"""Generated from Smithy shape ``com.amazonaws.workspaces#AccessPropertyValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

AccessPropertyValue: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: AccessPropertyValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessPropertyValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessPropertyValue value: {data!r}")
    return cast(AccessPropertyValue, data)
