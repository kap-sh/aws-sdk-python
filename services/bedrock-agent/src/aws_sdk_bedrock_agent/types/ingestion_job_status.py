"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

IngestionJobStatus: TypeAlias = Literal[
    "STARTING",
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "IN_PROGRESS",
        "COMPLETE",
        "FAILED",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_json(value: IngestionJobStatus) -> str:
    return value


def deserialize_json(data: str) -> IngestionJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionJobStatus value: {data!r}")
    return cast(IngestionJobStatus, data)
