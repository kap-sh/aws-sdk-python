"""Generated from Smithy shape ``com.amazonaws.cloud9#MemberPermissions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloud9.errors import DeserializationError

MemberPermissions: TypeAlias = Literal[
    "read-write",
    "read-only",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "read-write",
        "read-only",
    )
)


def serialize_aws_json_1_1(value: MemberPermissions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MemberPermissions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberPermissions value: {data!r}")
    return cast(MemberPermissions, data)
