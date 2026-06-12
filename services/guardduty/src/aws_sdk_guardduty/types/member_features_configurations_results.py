"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberFeaturesConfigurationsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.member_features_configuration_result

MemberFeaturesConfigurationsResults: TypeAlias = list[
    "aws_sdk_guardduty.types.member_features_configuration_result.MemberFeaturesConfigurationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberFeaturesConfigurationsResults) -> list:
    import aws_sdk_guardduty.types.member_features_configuration_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.member_features_configuration_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemberFeaturesConfigurationsResults:
    import aws_sdk_guardduty.types.member_features_configuration_result

    out: MemberFeaturesConfigurationsResults = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.member_features_configuration_result.deserialize_json(
                item
            )
        )
    return out
