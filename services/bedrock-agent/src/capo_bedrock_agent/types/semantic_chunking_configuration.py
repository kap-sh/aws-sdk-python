"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SemanticChunkingConfiguration``."""

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError


class SemanticChunkingConfiguration(TypedDict, closed=True):
    max_tokens: "int"
    """<p>The maximum number of tokens that a chunk can contain.</p>"""
    buffer_size: "int"
    """<p>The buffer size.</p>"""
    breakpoint_percentile_threshold: "int"
    """<p>The dissimilarity threshold for splitting chunks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticChunkingConfiguration) -> dict:
    out: dict = {}
    out["maxTokens"] = value["max_tokens"]
    out["bufferSize"] = value["buffer_size"]
    out["breakpointPercentileThreshold"] = value["breakpoint_percentile_threshold"]
    return out


def deserialize_json(data: dict) -> SemanticChunkingConfiguration:
    out: SemanticChunkingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("maxTokens") is not None:
        out["max_tokens"] = data["maxTokens"]
    else:
        raise DeserializationError("SemanticChunkingConfiguration.max_tokens required")
    if data.get("bufferSize") is not None:
        out["buffer_size"] = data["bufferSize"]
    else:
        raise DeserializationError("SemanticChunkingConfiguration.buffer_size required")
    if data.get("breakpointPercentileThreshold") is not None:
        out["breakpoint_percentile_threshold"] = data["breakpointPercentileThreshold"]
    else:
        raise DeserializationError(
            "SemanticChunkingConfiguration.breakpoint_percentile_threshold required"
        )
    return out
