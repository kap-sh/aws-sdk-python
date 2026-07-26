"""Generated from Smithy shape ``com.amazonaws.guardduty#AnomalyProfileFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.anomaly_profile_feature_objects
    import capo_guardduty.types.string

AnomalyProfileFeatures: TypeAlias = dict[
    "capo_guardduty.types.string.String",
    "capo_guardduty.types.anomaly_profile_feature_objects.AnomalyProfileFeatureObjects",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AnomalyProfileFeatures) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_guardduty.types.anomaly_profile_feature_objects

        out[key] = capo_guardduty.types.anomaly_profile_feature_objects.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> AnomalyProfileFeatures:
    out: AnomalyProfileFeatures = {}
    for key, value in data.items():
        import capo_guardduty.types.anomaly_profile_feature_objects

        out[key] = (
            capo_guardduty.types.anomaly_profile_feature_objects.deserialize_json(value)
        )
    return out
