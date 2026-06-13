"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#PlatformTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

PlatformTypeEnum: TypeAlias = Literal[
    "Windows",
    "Windows BYOL",
    "Linux/UNIX",
    "Ubuntu Pro Linux",
    "Red Hat Enterprise Linux",
    "Red Hat BYOL Linux",
    "SUSE Linux",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Windows",
        "Windows BYOL",
        "Linux/UNIX",
        "Ubuntu Pro Linux",
        "Red Hat Enterprise Linux",
        "Red Hat BYOL Linux",
        "SUSE Linux",
    )
)


def serialize_aws_json_1_0(value: PlatformTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PlatformTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlatformTypeEnum value: {data!r}")
    return cast(PlatformTypeEnum, data)
