"""Generated from Smithy shape ``com.amazonaws.odb#PermissionLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

PermissionLevel: TypeAlias = Literal[
    "RESTRICTED",
    "UNRESTRICTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESTRICTED",
        "UNRESTRICTED",
    )
)


def serialize_aws_json_1_0(value: PermissionLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PermissionLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionLevel value: {data!r}")
    return cast(PermissionLevel, data)
