"""Generated from Smithy shape ``com.amazonaws.iotsitewise#HierarchyMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.hierarchy_mapping

HierarchyMappings: TypeAlias = list[
    "aws_sdk_iotsitewise.types.hierarchy_mapping.HierarchyMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyMappings) -> list:
    import aws_sdk_iotsitewise.types.hierarchy_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.hierarchy_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> HierarchyMappings:
    import aws_sdk_iotsitewise.types.hierarchy_mapping

    out: HierarchyMappings = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.hierarchy_mapping.deserialize_json(item))
    return out
