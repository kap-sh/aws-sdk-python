"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.nullable_boolean
    import aws_sdk_chime_sdk_voice.types.sip_rule_name
    import aws_sdk_chime_sdk_voice.types.sip_rule_target_application_list
    import aws_sdk_chime_sdk_voice.types.sip_rule_trigger_type


class CreateSipRuleRequest(TypedDict):
    name: "aws_sdk_chime_sdk_voice.types.sip_rule_name.SipRuleName"
    """<p>The name of the SIP rule.</p>"""
    trigger_type: (
        "aws_sdk_chime_sdk_voice.types.sip_rule_trigger_type.SipRuleTriggerType"
    )
    """<p>The type of trigger assigned to the SIP rule in <code>TriggerValue</code>, currently <code>RequestUriHostname</code> or <code>ToPhoneNumber</code>.</p>"""
    trigger_value: "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>If <code>TriggerType</code> is <code>RequestUriHostname</code>, the value can be the outbound host name of a Voice Connector. If <code>TriggerType</code> is <code>ToPhoneNumber</code>, the value can be a customer-owned phone number in the E164 format. The <code>SipMediaApplication</code> specified in the <code>SipRule</code> is triggered if the request URI in an incoming SIP request matches the <code>RequestUriHostname</code>, or if the <code>To</code> header in the incoming SIP request matches the <code>ToPhoneNumber</code> value.</p>"""
    disabled: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Disables or enables a SIP rule. You must disable SIP rules before you can delete them.</p>"""
    target_applications: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_rule_target_application_list.SipRuleTargetApplicationList"
    ]
    """<p>List of SIP media applications, with priority and AWS Region. Only one SIP application per AWS Region can be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_chime_sdk_voice.types.sip_rule_trigger_type

    out["TriggerType"] = (
        aws_sdk_chime_sdk_voice.types.sip_rule_trigger_type.serialize_json(
            value["trigger_type"]
        )
    )
    out["TriggerValue"] = value["trigger_value"]
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


def deserialize_json(data: dict) -> CreateSipRuleRequest:
    out: CreateSipRuleRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSipRuleRequest.name required")
    if "TriggerType" in data:
        import aws_sdk_chime_sdk_voice.types.sip_rule_trigger_type

        out["trigger_type"] = (
            aws_sdk_chime_sdk_voice.types.sip_rule_trigger_type.deserialize_json(
                data["TriggerType"]
            )
        )
    else:
        raise DeserializationError("CreateSipRuleRequest.trigger_type required")
    if "TriggerValue" in data:
        out["trigger_value"] = data["TriggerValue"]
    else:
        raise DeserializationError("CreateSipRuleRequest.trigger_value required")
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
