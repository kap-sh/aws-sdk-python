"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorFeaturesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_guard_duty_detector_features_details

AwsGuardDutyDetectorFeaturesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_guard_duty_detector_features_details.AwsGuardDutyDetectorFeaturesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorFeaturesList) -> list:
    import aws_sdk_securityhub.types.aws_guard_duty_detector_features_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_guard_duty_detector_features_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsGuardDutyDetectorFeaturesList:
    import aws_sdk_securityhub.types.aws_guard_duty_detector_features_details

    out: AwsGuardDutyDetectorFeaturesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_guard_duty_detector_features_details.deserialize_json(
                item
            )
        )
    return out
