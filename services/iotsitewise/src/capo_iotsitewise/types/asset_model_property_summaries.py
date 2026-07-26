"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelPropertySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_model_property_summary

AssetModelPropertySummaries: TypeAlias = list[
    "capo_iotsitewise.types.asset_model_property_summary.AssetModelPropertySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelPropertySummaries) -> list:
    import capo_iotsitewise.types.asset_model_property_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.asset_model_property_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetModelPropertySummaries:
    import capo_iotsitewise.types.asset_model_property_summary

    out: AssetModelPropertySummaries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.asset_model_property_summary.deserialize_json(item)
        )
    return out
