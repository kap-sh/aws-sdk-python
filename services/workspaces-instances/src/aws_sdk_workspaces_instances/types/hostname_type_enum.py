"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HostnameTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

HostnameTypeEnum: TypeAlias = Literal[
    "ip-name",
    "resource-name",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ip-name",
        "resource-name",
    )
)


def serialize_aws_json_1_0(value: HostnameTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HostnameTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HostnameTypeEnum value: {data!r}")
    return cast(HostnameTypeEnum, data)
