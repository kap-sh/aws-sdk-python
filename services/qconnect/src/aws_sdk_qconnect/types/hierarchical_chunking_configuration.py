"""Generated from Smithy shape ``com.amazonaws.qconnect#HierarchicalChunkingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.hierarchical_chunking_level_configurations


class HierarchicalChunkingConfiguration(TypedDict):
    level_configurations: "aws_sdk_qconnect.types.hierarchical_chunking_level_configurations.HierarchicalChunkingLevelConfigurations"
    """<p>Token settings for each layer.</p>"""
    overlap_tokens: "int"
    """<p>The number of tokens to repeat across chunks in the same layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchicalChunkingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.hierarchical_chunking_level_configurations

    out["levelConfigurations"] = (
        aws_sdk_qconnect.types.hierarchical_chunking_level_configurations.serialize_json(
            value["level_configurations"]
        )
    )
    out["overlapTokens"] = value["overlap_tokens"]
    return out


def deserialize_json(data: dict) -> HierarchicalChunkingConfiguration:
    out: HierarchicalChunkingConfiguration = {}  # type: ignore[typeddict-item]
    if "levelConfigurations" in data:
        import aws_sdk_qconnect.types.hierarchical_chunking_level_configurations

        out["level_configurations"] = (
            aws_sdk_qconnect.types.hierarchical_chunking_level_configurations.deserialize_json(
                data["levelConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "HierarchicalChunkingConfiguration.level_configurations required"
        )
    if "overlapTokens" in data:
        out["overlap_tokens"] = data["overlapTokens"]
    else:
        raise DeserializationError(
            "HierarchicalChunkingConfiguration.overlap_tokens required"
        )
    return out
