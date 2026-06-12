"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorFeatureConfigurationsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_feature_configuration_result

DetectorFeatureConfigurationsResults: TypeAlias = list[
    "aws_sdk_guardduty.types.detector_feature_configuration_result.DetectorFeatureConfigurationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorFeatureConfigurationsResults) -> list:
    import aws_sdk_guardduty.types.detector_feature_configuration_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.detector_feature_configuration_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DetectorFeatureConfigurationsResults:
    import aws_sdk_guardduty.types.detector_feature_configuration_result

    out: DetectorFeatureConfigurationsResults = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.detector_feature_configuration_result.deserialize_json(
                item
            )
        )
    return out
