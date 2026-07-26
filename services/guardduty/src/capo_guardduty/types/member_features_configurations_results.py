"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberFeaturesConfigurationsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.member_features_configuration_result

MemberFeaturesConfigurationsResults: TypeAlias = list[
    "capo_guardduty.types.member_features_configuration_result.MemberFeaturesConfigurationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberFeaturesConfigurationsResults) -> list:
    import capo_guardduty.types.member_features_configuration_result

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.member_features_configuration_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemberFeaturesConfigurationsResults:
    import capo_guardduty.types.member_features_configuration_result

    out: MemberFeaturesConfigurationsResults = []
    for item in data:
        out.append(
            capo_guardduty.types.member_features_configuration_result.deserialize_json(
                item
            )
        )
    return out
