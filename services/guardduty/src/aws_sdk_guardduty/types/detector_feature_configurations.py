"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorFeatureConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_feature_configuration

DetectorFeatureConfigurations: TypeAlias = list[
    "aws_sdk_guardduty.types.detector_feature_configuration.DetectorFeatureConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorFeatureConfigurations) -> list:
    import aws_sdk_guardduty.types.detector_feature_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.detector_feature_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DetectorFeatureConfigurations:
    import aws_sdk_guardduty.types.detector_feature_configuration

    out: DetectorFeatureConfigurations = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.detector_feature_configuration.deserialize_json(
                item
            )
        )
    return out
