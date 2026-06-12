"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataDeletionPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

DataDeletionPolicy: TypeAlias = Literal[
    "RETAIN",
    "DELETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RETAIN",
        "DELETE",
    )
)


def serialize_json(value: DataDeletionPolicy) -> str:
    return value


def deserialize_json(data: str) -> DataDeletionPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataDeletionPolicy value: {data!r}")
    return cast(DataDeletionPolicy, data)
