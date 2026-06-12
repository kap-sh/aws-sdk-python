"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RerankingMetadataSelectionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

RerankingMetadataSelectionMode: TypeAlias = Literal[
    "SELECTIVE",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELECTIVE",
        "ALL",
    )
)


def serialize_json(value: RerankingMetadataSelectionMode) -> str:
    return value


def deserialize_json(data: str) -> RerankingMetadataSelectionMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RerankingMetadataSelectionMode value: {data!r}"
        )
    return cast(RerankingMetadataSelectionMode, data)
