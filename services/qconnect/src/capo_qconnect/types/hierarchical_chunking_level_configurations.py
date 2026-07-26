"""Generated from Smithy shape ``com.amazonaws.qconnect#HierarchicalChunkingLevelConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.hierarchical_chunking_level_configuration

HierarchicalChunkingLevelConfigurations: TypeAlias = list[
    "capo_qconnect.types.hierarchical_chunking_level_configuration.HierarchicalChunkingLevelConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchicalChunkingLevelConfigurations) -> list:
    import capo_qconnect.types.hierarchical_chunking_level_configuration

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.hierarchical_chunking_level_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HierarchicalChunkingLevelConfigurations:
    import capo_qconnect.types.hierarchical_chunking_level_configuration

    out: HierarchicalChunkingLevelConfigurations = []
    for item in data:
        out.append(
            capo_qconnect.types.hierarchical_chunking_level_configuration.deserialize_json(
                item
            )
        )
    return out
