"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

DocumentStatus: TypeAlias = Literal[
    "INDEXED",
    "PARTIALLY_INDEXED",
    "PENDING",
    "FAILED",
    "METADATA_PARTIALLY_INDEXED",
    "METADATA_UPDATE_FAILED",
    "IGNORED",
    "NOT_FOUND",
    "STARTING",
    "IN_PROGRESS",
    "DELETING",
    "DELETE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INDEXED",
        "PARTIALLY_INDEXED",
        "PENDING",
        "FAILED",
        "METADATA_PARTIALLY_INDEXED",
        "METADATA_UPDATE_FAILED",
        "IGNORED",
        "NOT_FOUND",
        "STARTING",
        "IN_PROGRESS",
        "DELETING",
        "DELETE_IN_PROGRESS",
    )
)


def serialize_json(value: DocumentStatus) -> str:
    return value


def deserialize_json(data: str) -> DocumentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentStatus value: {data!r}")
    return cast(DocumentStatus, data)
