"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FixedSizeChunkingConfiguration``."""

from typing import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError


class FixedSizeChunkingConfiguration(TypedDict):
    max_tokens: "int"
    """<p>The maximum number of tokens to include in a chunk.</p>"""
    overlap_percentage: "int"
    """<p>The percentage of overlap between adjacent chunks of a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedSizeChunkingConfiguration) -> dict:
    out: dict = {}
    out["maxTokens"] = value["max_tokens"]
    out["overlapPercentage"] = value["overlap_percentage"]
    return out


def deserialize_json(data: dict) -> FixedSizeChunkingConfiguration:
    out: FixedSizeChunkingConfiguration = {}  # type: ignore[typeddict-item]
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    else:
        raise DeserializationError("FixedSizeChunkingConfiguration.max_tokens required")
    if "overlapPercentage" in data:
        out["overlap_percentage"] = data["overlapPercentage"]
    else:
        raise DeserializationError(
            "FixedSizeChunkingConfiguration.overlap_percentage required"
        )
    return out
