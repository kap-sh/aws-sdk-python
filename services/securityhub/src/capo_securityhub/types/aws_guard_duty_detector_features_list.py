"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsGuardDutyDetectorFeaturesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_guard_duty_detector_features_details

AwsGuardDutyDetectorFeaturesList: TypeAlias = list[
    "capo_securityhub.types.aws_guard_duty_detector_features_details.AwsGuardDutyDetectorFeaturesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsGuardDutyDetectorFeaturesList) -> list:
    import capo_securityhub.types.aws_guard_duty_detector_features_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_guard_duty_detector_features_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsGuardDutyDetectorFeaturesList:
    import capo_securityhub.types.aws_guard_duty_detector_features_details

    out: AwsGuardDutyDetectorFeaturesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_guard_duty_detector_features_details.deserialize_json(
                item
            )
        )
    return out
