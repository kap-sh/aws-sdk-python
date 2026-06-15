"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

RegistryRecordStatus: TypeAlias = Literal[
    "DRAFT",
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "DEPRECATED",
    "CREATING",
    "UPDATING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "PENDING_APPROVAL",
        "APPROVED",
        "REJECTED",
        "DEPRECATED",
        "CREATING",
        "UPDATING",
        "CREATE_FAILED",
        "UPDATE_FAILED",
    )
)


def serialize_json(value: RegistryRecordStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistryRecordStatus value: {data!r}")
    return cast(RegistryRecordStatus, data)
