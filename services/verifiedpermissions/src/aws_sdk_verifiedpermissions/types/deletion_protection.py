"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletionProtection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

DeletionProtection: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: DeletionProtection) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DeletionProtection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeletionProtection value: {data!r}")
    return cast(DeletionProtection, data)
