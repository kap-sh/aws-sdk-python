"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InterfaceTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

InterfaceTypeEnum: TypeAlias = Literal[
    "interface",
    "efa",
    "efa-only",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "interface",
        "efa",
        "efa-only",
    )
)


def serialize_aws_json_1_0(value: InterfaceTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InterfaceTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InterfaceTypeEnum value: {data!r}")
    return cast(InterfaceTypeEnum, data)
