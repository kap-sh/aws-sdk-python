"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListProtectConfigurationRuleSetNumberOverridesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list


class ListProtectConfigurationRuleSetNumberOverridesResult(TypedDict):
    protect_configuration_arn: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_arn.ProtectConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the protect configuration.</p>"""
    protect_configuration_id: "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_id.ProtectConfigurationId"
    """<p>The unique identifier for the protect configuration.</p>"""
    rule_set_number_overrides: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list.ProtectConfigurationRuleSetNumberOverrideList"
    ]
    """<p>An array of RuleSetNumberOverrides objects.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListProtectConfigurationRuleSetNumberOverridesResult,
) -> dict:
    out: dict = {}
    out["ProtectConfigurationArn"] = value["protect_configuration_arn"]
    out["ProtectConfigurationId"] = value["protect_configuration_id"]
    if "rule_set_number_overrides" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list

        out["RuleSetNumberOverrides"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list.serialize_aws_json_1_0(
                value["rule_set_number_overrides"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListProtectConfigurationRuleSetNumberOverridesResult:
    out: ListProtectConfigurationRuleSetNumberOverridesResult = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurationArn" in data:
        out["protect_configuration_arn"] = data["ProtectConfigurationArn"]
    else:
        raise DeserializationError(
            "ListProtectConfigurationRuleSetNumberOverridesResult.protect_configuration_arn required"
        )
    if "ProtectConfigurationId" in data:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    else:
        raise DeserializationError(
            "ListProtectConfigurationRuleSetNumberOverridesResult.protect_configuration_id required"
        )
    if "RuleSetNumberOverrides" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list

        out["rule_set_number_overrides"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_rule_set_number_override_list.deserialize_aws_json_1_0(
                data["RuleSetNumberOverrides"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
