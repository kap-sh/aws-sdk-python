"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.iso8601_timestamp
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.sip_rule_name
    import capo_chime_sdk_voice.types.sip_rule_target_application_list
    import capo_chime_sdk_voice.types.sip_rule_trigger_type


class SipRule(TypedDict, closed=True):
    sip_rule_id: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>A SIP rule's ID.</p>"""
    name: NotRequired["capo_chime_sdk_voice.types.sip_rule_name.SipRuleName"]
    """<p>A SIP rule's name.</p>"""
    disabled: NotRequired["capo_chime_sdk_voice.types.boolean.Boolean"]
    """<p>Indicates whether the SIP rule is enabled or disabled. You must disable a rule before you can delete it.</p>"""
    trigger_type: NotRequired[
        "capo_chime_sdk_voice.types.sip_rule_trigger_type.SipRuleTriggerType"
    ]
    """<p>The type of trigger set for a SIP rule, either a phone number or a URI request host name.</p>"""
    trigger_value: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The value set for a SIP rule's trigger type. Either a phone number or a URI hostname.</p>"""
    target_applications: NotRequired[
        "capo_chime_sdk_voice.types.sip_rule_target_application_list.SipRuleTargetApplicationList"
    ]
    """<p>The target SIP media application and other details, such as priority and AWS Region, to be specified in the SIP rule. Only one SIP rule per AWS Region can be provided.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the SIP rule was created, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the SIP rule was updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SipRule) -> dict:
    out: dict = {}
    if "sip_rule_id" in value:
        out["SipRuleId"] = value["sip_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "trigger_type" in value:
        import capo_chime_sdk_voice.types.sip_rule_trigger_type

        out["TriggerType"] = (
            capo_chime_sdk_voice.types.sip_rule_trigger_type.serialize_json(
                value["trigger_type"]
            )
        )
    if "trigger_value" in value:
        out["TriggerValue"] = value["trigger_value"]
    if "target_applications" in value:
        import capo_chime_sdk_voice.types.sip_rule_target_application_list

        out["TargetApplications"] = (
            capo_chime_sdk_voice.types.sip_rule_target_application_list.serialize_json(
                value["target_applications"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> SipRule:
    out: SipRule = {}  # type: ignore[typeddict-item]
    if "SipRuleId" in data:
        out["sip_rule_id"] = data["SipRuleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    if "TriggerType" in data:
        import capo_chime_sdk_voice.types.sip_rule_trigger_type

        out["trigger_type"] = (
            capo_chime_sdk_voice.types.sip_rule_trigger_type.deserialize_json(
                data["TriggerType"]
            )
        )
    if "TriggerValue" in data:
        out["trigger_value"] = data["TriggerValue"]
    if "TargetApplications" in data:
        import capo_chime_sdk_voice.types.sip_rule_target_application_list

        out["target_applications"] = (
            capo_chime_sdk_voice.types.sip_rule_target_application_list.deserialize_json(
                data["TargetApplications"]
            )
        )
    if "CreatedTimestamp" in data:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    return out
