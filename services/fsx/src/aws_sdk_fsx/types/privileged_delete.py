"""Generated from Smithy shape ``com.amazonaws.fsx#PrivilegedDelete``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

PrivilegedDelete: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "PERMANENTLY_DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "PERMANENTLY_DISABLED",
    )
)


def serialize_aws_json_1_1(value: PrivilegedDelete) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrivilegedDelete:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrivilegedDelete value: {data!r}")
    return cast(PrivilegedDelete, data)
