"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberFeaturesConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.member_features_configuration

MemberFeaturesConfigurations: TypeAlias = list[
    "capo_guardduty.types.member_features_configuration.MemberFeaturesConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberFeaturesConfigurations) -> list:
    import capo_guardduty.types.member_features_configuration

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.member_features_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemberFeaturesConfigurations:
    import capo_guardduty.types.member_features_configuration

    out: MemberFeaturesConfigurations = []
    for item in data:
        out.append(
            capo_guardduty.types.member_features_configuration.deserialize_json(item)
        )
    return out
