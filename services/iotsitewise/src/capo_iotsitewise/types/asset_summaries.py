"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_summary

AssetSummaries: TypeAlias = list["capo_iotsitewise.types.asset_summary.AssetSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetSummaries) -> list:
    import capo_iotsitewise.types.asset_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.asset_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetSummaries:
    import capo_iotsitewise.types.asset_summary

    out: AssetSummaries = []
    for item in data:
        out.append(capo_iotsitewise.types.asset_summary.deserialize_json(item))
    return out
