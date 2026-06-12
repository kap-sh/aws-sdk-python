"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorAdditionalConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_additional_configuration

DetectorAdditionalConfigurations: TypeAlias = list[
    "aws_sdk_guardduty.types.detector_additional_configuration.DetectorAdditionalConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorAdditionalConfigurations) -> list:
    import aws_sdk_guardduty.types.detector_additional_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.detector_additional_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DetectorAdditionalConfigurations:
    import aws_sdk_guardduty.types.detector_additional_configuration

    out: DetectorAdditionalConfigurations = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.detector_additional_configuration.deserialize_json(
                item
            )
        )
    return out
