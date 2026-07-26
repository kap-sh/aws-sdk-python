"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetRelationshipSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_relationship_summary

AssetRelationshipSummaries: TypeAlias = list[
    "capo_iotsitewise.types.asset_relationship_summary.AssetRelationshipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetRelationshipSummaries) -> list:
    import capo_iotsitewise.types.asset_relationship_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.asset_relationship_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetRelationshipSummaries:
    import capo_iotsitewise.types.asset_relationship_summary

    out: AssetRelationshipSummaries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.asset_relationship_summary.deserialize_json(item)
        )
    return out
