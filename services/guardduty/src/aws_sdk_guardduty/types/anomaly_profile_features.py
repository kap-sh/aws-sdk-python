"""Generated from Smithy shape ``com.amazonaws.guardduty#AnomalyProfileFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.anomaly_profile_feature_objects
    import aws_sdk_guardduty.types.string

AnomalyProfileFeatures: TypeAlias = dict[
    "aws_sdk_guardduty.types.string.String",
    "aws_sdk_guardduty.types.anomaly_profile_feature_objects.AnomalyProfileFeatureObjects",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AnomalyProfileFeatures) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_guardduty.types.anomaly_profile_feature_objects

        out[key] = (
            aws_sdk_guardduty.types.anomaly_profile_feature_objects.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> AnomalyProfileFeatures:
    out: AnomalyProfileFeatures = {}
    for key, value in data.items():
        import aws_sdk_guardduty.types.anomaly_profile_feature_objects

        out[key] = (
            aws_sdk_guardduty.types.anomaly_profile_feature_objects.deserialize_json(
                value
            )
        )
    return out
