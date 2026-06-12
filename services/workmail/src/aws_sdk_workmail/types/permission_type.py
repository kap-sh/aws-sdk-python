"""Generated from Smithy shape ``com.amazonaws.workmail#PermissionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

PermissionType: TypeAlias = Literal[
    "FULL_ACCESS",
    "SEND_AS",
    "SEND_ON_BEHALF",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_ACCESS",
        "SEND_AS",
        "SEND_ON_BEHALF",
    )
)


def serialize_aws_json_1_1(value: PermissionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PermissionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionType value: {data!r}")
    return cast(PermissionType, data)
