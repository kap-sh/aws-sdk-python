"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RegistryRecordStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p> The status of a registry record in its lifecycle.</p>"""
RegistryRecordStatus: TypeAlias = Literal[
    "DRAFT",
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "PENDING_APPROVAL",
        "APPROVED",
        "REJECTED",
        "DEPRECATED",
    )
)


def serialize_json(value: RegistryRecordStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistryRecordStatus value: {data!r}")
    return cast(RegistryRecordStatus, data)
