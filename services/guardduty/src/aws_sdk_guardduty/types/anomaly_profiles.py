"""Generated from Smithy shape ``com.amazonaws.guardduty#AnomalyProfiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.anomaly_profile_features
    import aws_sdk_guardduty.types.string

AnomalyProfiles: TypeAlias = dict[
    "aws_sdk_guardduty.types.string.String",
    "aws_sdk_guardduty.types.anomaly_profile_features.AnomalyProfileFeatures",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AnomalyProfiles) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_guardduty.types.anomaly_profile_features

        out[key] = aws_sdk_guardduty.types.anomaly_profile_features.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> AnomalyProfiles:
    out: AnomalyProfiles = {}
    for key, value in data.items():
        import aws_sdk_guardduty.types.anomaly_profile_features

        out[key] = aws_sdk_guardduty.types.anomaly_profile_features.deserialize_json(
            value
        )
    return out
