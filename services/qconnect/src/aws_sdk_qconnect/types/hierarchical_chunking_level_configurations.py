"""Generated from Smithy shape ``com.amazonaws.qconnect#HierarchicalChunkingLevelConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.hierarchical_chunking_level_configuration

HierarchicalChunkingLevelConfigurations: TypeAlias = list[
    "aws_sdk_qconnect.types.hierarchical_chunking_level_configuration.HierarchicalChunkingLevelConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchicalChunkingLevelConfigurations) -> list:
    import aws_sdk_qconnect.types.hierarchical_chunking_level_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.hierarchical_chunking_level_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HierarchicalChunkingLevelConfigurations:
    import aws_sdk_qconnect.types.hierarchical_chunking_level_configuration

    out: HierarchicalChunkingLevelConfigurations = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.hierarchical_chunking_level_configuration.deserialize_json(
                item
            )
        )
    return out
