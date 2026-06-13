"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HttpProtocolIpv6Enum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

HttpProtocolIpv6Enum: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def serialize_aws_json_1_0(value: HttpProtocolIpv6Enum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HttpProtocolIpv6Enum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HttpProtocolIpv6Enum value: {data!r}")
    return cast(HttpProtocolIpv6Enum, data)
