"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ResourceTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

ResourceTypeEnum: TypeAlias = Literal[
    "instance",
    "volume",
    "spot-instances-request",
    "network-interface",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "instance",
        "volume",
        "spot-instances-request",
        "network-interface",
    )
)


def serialize_aws_json_1_0(value: ResourceTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceTypeEnum value: {data!r}")
    return cast(ResourceTypeEnum, data)
