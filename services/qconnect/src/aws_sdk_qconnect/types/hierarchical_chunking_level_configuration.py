"""Generated from Smithy shape ``com.amazonaws.qconnect#HierarchicalChunkingLevelConfiguration``."""

from typing import TypedDict

from aws_sdk_qconnect.errors import DeserializationError


class HierarchicalChunkingLevelConfiguration(TypedDict):
    max_tokens: "int"
    """<p>The maximum number of tokens that a chunk can contain in this layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchicalChunkingLevelConfiguration) -> dict:
    out: dict = {}
    out["maxTokens"] = value["max_tokens"]
    return out


def deserialize_json(data: dict) -> HierarchicalChunkingLevelConfiguration:
    out: HierarchicalChunkingLevelConfiguration = {}  # type: ignore[typeddict-item]
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    else:
        raise DeserializationError(
            "HierarchicalChunkingLevelConfiguration.max_tokens required"
        )
    return out
