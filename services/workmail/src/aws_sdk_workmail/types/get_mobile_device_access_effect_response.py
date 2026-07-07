"""Generated from Smithy shape ``com.amazonaws.workmail#GetMobileDeviceAccessEffectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mobile_device_access_matched_rule_list
    import aws_sdk_workmail.types.mobile_device_access_rule_effect


class GetMobileDeviceAccessEffectResponse(TypedDict, closed=True):
    effect: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect"
    ]
    """<p>The effect of the simulated access, <code>ALLOW</code> or <code>DENY</code>, after evaluating mobile device access rules in the WorkMail organization for the simulated user parameters.</p>"""
    matched_rules: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_matched_rule_list.MobileDeviceAccessMatchedRuleList"
    ]
    """<p>A list of the rules which matched the simulated user input and produced the effect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMobileDeviceAccessEffectResponse) -> dict:
    out: dict = {}
    if "effect" in value:
        import aws_sdk_workmail.types.mobile_device_access_rule_effect

        out["Effect"] = (
            aws_sdk_workmail.types.mobile_device_access_rule_effect.serialize_aws_json_1_1(
                value["effect"]
            )
        )
    if "matched_rules" in value:
        import aws_sdk_workmail.types.mobile_device_access_matched_rule_list

        out["MatchedRules"] = (
            aws_sdk_workmail.types.mobile_device_access_matched_rule_list.serialize_aws_json_1_1(
                value["matched_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMobileDeviceAccessEffectResponse:
    out: GetMobileDeviceAccessEffectResponse = {}  # type: ignore[typeddict-item]
    if "Effect" in data:
        import aws_sdk_workmail.types.mobile_device_access_rule_effect

        out["effect"] = (
            aws_sdk_workmail.types.mobile_device_access_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    if "MatchedRules" in data:
        import aws_sdk_workmail.types.mobile_device_access_matched_rule_list

        out["matched_rules"] = (
            aws_sdk_workmail.types.mobile_device_access_matched_rule_list.deserialize_aws_json_1_1(
                data["MatchedRules"]
            )
        )
    return out
