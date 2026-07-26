"""Generated from Smithy shape ``com.amazonaws.guardduty#Behavior``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.anomaly_unusual_behavior_feature
    import capo_guardduty.types.string

Behavior: TypeAlias = dict[
    "capo_guardduty.types.string.String",
    "capo_guardduty.types.anomaly_unusual_behavior_feature.AnomalyUnusualBehaviorFeature",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Behavior) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_guardduty.types.anomaly_unusual_behavior_feature

        out[key] = capo_guardduty.types.anomaly_unusual_behavior_feature.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> Behavior:
    out: Behavior = {}
    for key, value in data.items():
        import capo_guardduty.types.anomaly_unusual_behavior_feature

        out[key] = (
            capo_guardduty.types.anomaly_unusual_behavior_feature.deserialize_json(
                value
            )
        )
    return out
