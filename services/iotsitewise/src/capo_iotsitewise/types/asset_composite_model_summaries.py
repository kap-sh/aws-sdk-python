"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetCompositeModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_composite_model_summary

AssetCompositeModelSummaries: TypeAlias = list[
    "capo_iotsitewise.types.asset_composite_model_summary.AssetCompositeModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetCompositeModelSummaries) -> list:
    import capo_iotsitewise.types.asset_composite_model_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.asset_composite_model_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetCompositeModelSummaries:
    import capo_iotsitewise.types.asset_composite_model_summary

    out: AssetCompositeModelSummaries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.asset_composite_model_summary.deserialize_json(item)
        )
    return out
