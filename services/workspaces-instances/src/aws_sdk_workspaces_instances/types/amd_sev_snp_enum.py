"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AmdSevSnpEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

AmdSevSnpEnum: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: AmdSevSnpEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AmdSevSnpEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AmdSevSnpEnum value: {data!r}")
    return cast(AmdSevSnpEnum, data)
