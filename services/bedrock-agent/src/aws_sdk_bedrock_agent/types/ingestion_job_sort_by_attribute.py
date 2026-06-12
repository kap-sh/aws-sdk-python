"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobSortByAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

IngestionJobSortByAttribute: TypeAlias = Literal[
    "STATUS",
    "STARTED_AT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATUS",
        "STARTED_AT",
    )
)


def serialize_json(value: IngestionJobSortByAttribute) -> str:
    return value


def deserialize_json(data: str) -> IngestionJobSortByAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngestionJobSortByAttribute value: {data!r}"
        )
    return cast(IngestionJobSortByAttribute, data)
