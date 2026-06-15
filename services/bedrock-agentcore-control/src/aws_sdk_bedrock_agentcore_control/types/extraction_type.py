"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ExtractionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

"""<p>The extraction type for a metadata field, determining how the value is obtained during memory processing.</p>"""
ExtractionType: TypeAlias = Literal[
    "LLM_INFERRED",
    "STRICTLY_CONSISTENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LLM_INFERRED",
        "STRICTLY_CONSISTENT",
    )
)


def serialize_json(value: ExtractionType) -> str:
    return value


def deserialize_json(data: str) -> ExtractionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExtractionType value: {data!r}")
    return cast(ExtractionType, data)
