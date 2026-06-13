"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AutoRecoveryEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

AutoRecoveryEnum: TypeAlias = Literal[
    "disabled",
    "default",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "default",
    )
)


def serialize_aws_json_1_0(value: AutoRecoveryEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutoRecoveryEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoRecoveryEnum value: {data!r}")
    return cast(AutoRecoveryEnum, data)
