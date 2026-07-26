"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorFeatureConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.detector_feature_configuration

DetectorFeatureConfigurations: TypeAlias = list[
    "capo_guardduty.types.detector_feature_configuration.DetectorFeatureConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorFeatureConfigurations) -> list:
    import capo_guardduty.types.detector_feature_configuration

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.detector_feature_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DetectorFeatureConfigurations:
    import capo_guardduty.types.detector_feature_configuration

    out: DetectorFeatureConfigurations = []
    for item in data:
        out.append(
            capo_guardduty.types.detector_feature_configuration.deserialize_json(item)
        )
    return out
