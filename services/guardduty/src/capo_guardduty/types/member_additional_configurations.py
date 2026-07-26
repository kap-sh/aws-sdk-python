"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberAdditionalConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.member_additional_configuration

MemberAdditionalConfigurations: TypeAlias = list[
    "capo_guardduty.types.member_additional_configuration.MemberAdditionalConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberAdditionalConfigurations) -> list:
    import capo_guardduty.types.member_additional_configuration

    out: list = []
    for item in value:
        out.append(
            capo_guardduty.types.member_additional_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemberAdditionalConfigurations:
    import capo_guardduty.types.member_additional_configuration

    out: MemberAdditionalConfigurations = []
    for item in data:
        out.append(
            capo_guardduty.types.member_additional_configuration.deserialize_json(item)
        )
    return out
