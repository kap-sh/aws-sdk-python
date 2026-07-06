"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateSipRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.nullable_boolean
    import aws_sdk_chime_sdk_voice.types.sip_rule_name
    import aws_sdk_chime_sdk_voice.types.sip_rule_target_application_list


class UpdateSipRuleRequest(TypedDict, closed=True):
    sip_rule_id: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The SIP rule ID.</p>"""
    name: "aws_sdk_chime_sdk_voice.types.sip_rule_name.SipRuleName"
    """<p>The new name for the specified SIP rule.</p>"""
    disabled: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>The new value that indicates whether the rule is disabled.</p>"""
    target_applications: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_rule_target_application_list.SipRuleTargetApplicationList"
    ]
    """<p>The new list of target applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSipRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "target_applications" in value:
        import aws_sdk_chime_sdk_voice.types.sip_rule_target_application_list

        out["TargetApplications"] = (
            aws_sdk_chime_sdk_voice.types.sip_rule_target_application_list.serialize_json(
                value["target_applications"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSipRuleRequest:
    out: UpdateSipRuleRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateSipRuleRequest.name required")
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    if "TargetApplications" in data:
        import aws_sdk_chime_sdk_voice.types.sip_rule_target_application_list

        out["target_applications"] = (
            aws_sdk_chime_sdk_voice.types.sip_rule_target_application_list.deserialize_json(
                data["TargetApplications"]
            )
        )
    return out
