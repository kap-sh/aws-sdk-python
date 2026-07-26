"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberAdditionalConfigurationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.member_additional_configuration_result

MemberAdditionalConfigurationResults: TypeAlias = list[
    "capo_guardduty.types.member_additional_configuration_result.MemberAdditionalConfigurationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberAdditionalConfigurationResults) -> list:
    import capo_guardduty.types.member_additional_configuration_result

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.member_additional_configuration_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemberAdditionalConfigurationResults:
    import capo_guardduty.types.member_additional_configuration_result

    out: MemberAdditionalConfigurationResults = []
    for item in data:
        out.append(
            capo_guardduty.types.member_additional_configuration_result.deserialize_json(
                item
            )
        )
    return out
