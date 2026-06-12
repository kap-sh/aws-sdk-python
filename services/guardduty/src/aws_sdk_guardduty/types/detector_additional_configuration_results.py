"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorAdditionalConfigurationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_additional_configuration_result

DetectorAdditionalConfigurationResults: TypeAlias = list[
    "aws_sdk_guardduty.types.detector_additional_configuration_result.DetectorAdditionalConfigurationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorAdditionalConfigurationResults) -> list:
    import aws_sdk_guardduty.types.detector_additional_configuration_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.detector_additional_configuration_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DetectorAdditionalConfigurationResults:
    import aws_sdk_guardduty.types.detector_additional_configuration_result

    out: DetectorAdditionalConfigurationResults = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.detector_additional_configuration_result.deserialize_json(
                item
            )
        )
    return out
