"""Generated from Smithy shape ``com.amazonaws.qconnect#SemanticChunkingConfiguration``."""

from typing import TypedDict

from aws_sdk_qconnect.errors import DeserializationError


class SemanticChunkingConfiguration(TypedDict):
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
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    else:
        raise DeserializationError("SemanticChunkingConfiguration.max_tokens required")
    if "bufferSize" in data:
        out["buffer_size"] = data["bufferSize"]
    else:
        raise DeserializationError("SemanticChunkingConfiguration.buffer_size required")
    if "breakpointPercentileThreshold" in data:
        out["breakpoint_percentile_threshold"] = data["breakpointPercentileThreshold"]
    else:
        raise DeserializationError(
            "SemanticChunkingConfiguration.breakpoint_percentile_threshold required"
        )
    return out
