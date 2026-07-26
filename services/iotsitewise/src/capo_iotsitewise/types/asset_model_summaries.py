"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_summary

AssetModelSummaries: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_summary.AssetModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelSummaries) -> list:
    import capo_iotsitewise.types.asset_model_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.asset_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetModelSummaries:
    import capo_iotsitewise.types.asset_model_summary

    out: AssetModelSummaries = []
    for item in data:
        out.append(capo_iotsitewise.types.asset_model_summary.deserialize_json(item))
    return out
