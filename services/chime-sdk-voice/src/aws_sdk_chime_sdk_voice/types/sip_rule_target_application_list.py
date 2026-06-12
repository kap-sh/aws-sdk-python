"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipRuleTargetApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sip_rule_target_application

SipRuleTargetApplicationList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.sip_rule_target_application.SipRuleTargetApplication"
]


# --- restJson1 ser/de ---
def serialize_json(value: SipRuleTargetApplicationList) -> list:
    import aws_sdk_chime_sdk_voice.types.sip_rule_target_application

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.sip_rule_target_application.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SipRuleTargetApplicationList:
    import aws_sdk_chime_sdk_voice.types.sip_rule_target_application

    out: SipRuleTargetApplicationList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.sip_rule_target_application.deserialize_json(
                item
            )
        )
    return out
