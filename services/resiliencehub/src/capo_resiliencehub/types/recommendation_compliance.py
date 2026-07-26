"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationCompliance``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.disruption_type
    import capo_resiliencehub.types.recommendation_disruption_compliance

RecommendationCompliance: TypeAlias = dict[
    "capo_resiliencehub.types.disruption_type.DisruptionType",
    "capo_resiliencehub.types.recommendation_disruption_compliance.RecommendationDisruptionCompliance",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RecommendationCompliance) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_resiliencehub.types.disruption_type
        import capo_resiliencehub.types.recommendation_disruption_compliance

        out[capo_resiliencehub.types.disruption_type.serialize_json(key)] = (
            capo_resiliencehub.types.recommendation_disruption_compliance.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> RecommendationCompliance:
    out: RecommendationCompliance = {}
    for key, value in data.items():
        import capo_resiliencehub.types.disruption_type
        import capo_resiliencehub.types.recommendation_disruption_compliance

        out[capo_resiliencehub.types.disruption_type.deserialize_json(key)] = (
            capo_resiliencehub.types.recommendation_disruption_compliance.deserialize_json(
                value
            )
        )
    return out
