"""Generated from Smithy shape ``com.amazonaws.finspace#KxNodeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_node

KxNodeSummaries: TypeAlias = list["capo_finspace.types.kx_node.KxNode"]


# --- restJson1 ser/de ---
def serialize_json(value: KxNodeSummaries) -> list:
    import capo_finspace.types.kx_node

    out: list = []
    for item in value:
        out.append(capo_finspace.types.kx_node.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxNodeSummaries:
    import capo_finspace.types.kx_node

    out: KxNodeSummaries = []
    for item in data:
        out.append(capo_finspace.types.kx_node.deserialize_json(item))
    return out
