"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DisassociateModeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

DisassociateModeEnum: TypeAlias = Literal[
    "FORCE",
    "NO_FORCE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FORCE",
        "NO_FORCE",
    )
)


def serialize_aws_json_1_0(value: DisassociateModeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DisassociateModeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DisassociateModeEnum value: {data!r}")
    return cast(DisassociateModeEnum, data)
