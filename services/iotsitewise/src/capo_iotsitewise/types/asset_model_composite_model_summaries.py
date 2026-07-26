"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelCompositeModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_composite_model_summary

AssetModelCompositeModelSummaries: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_composite_model_summary.AssetModelCompositeModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelCompositeModelSummaries) -> list:
    import capo_iotsitewise.types.asset_model_composite_model_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.asset_model_composite_model_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetModelCompositeModelSummaries:
    import capo_iotsitewise.types.asset_model_composite_model_summary

    out: AssetModelCompositeModelSummaries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.asset_model_composite_model_summary.deserialize_json(
                item
            )
        )
    return out
