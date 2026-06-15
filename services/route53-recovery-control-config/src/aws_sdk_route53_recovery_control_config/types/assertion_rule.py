"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#AssertionRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__integer
    import aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import aws_sdk_route53_recovery_control_config.types.__string_min12_max12_pattern_d12
    import aws_sdk_route53_recovery_control_config.types.rule_config
    import aws_sdk_route53_recovery_control_config.types.status


class AssertionRule(TypedDict):
    asserted_controls: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.__listOf__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The routing controls that are part of transactions that are evaluated to determine if a request to change a routing control state is allowed. For example, you might include three routing controls, one for each of three Amazon Web Services Regions.</p>"""
    control_panel_arn: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the control panel.</p>"""
    name: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>Name of the assertion rule. You can use any non-white space character in the name.</p>"""
    rule_config: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.rule_config.RuleConfig"
    ]
    """<p>The criteria that you set for specific assertion routing controls (AssertedControls) that designate how many routing control states must be ON as the result of a transaction. For example, if you have three assertion routing controls, you might specify ATLEAST 2 for your rule configuration. This means that at least two assertion routing control states must be ON, so that at least two Amazon Web Services Regions have traffic flowing to them.</p>"""
    safety_rule_arn: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the assertion rule.</p>"""
    status: NotRequired["aws_sdk_route53_recovery_control_config.types.status.Status"]
    """<p>The deployment status of an assertion rule. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</p>"""
    wait_period_ms: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__integer.__integer"
    ]
    r"""<p>An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent \"flapping\" of state. The wait period is 5000 ms by default, but you can choose a custom value.</p>"""
    owner: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min12_max12_pattern_d12.__stringMin12Max12PatternD12"
    ]
    """<p>The Amazon Web Services account ID of the assertion rule owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssertionRule) -> dict:
    out: dict = {}
    if "asserted_controls" in value:
        import aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["AssertedControls"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.serialize_json(
                value["asserted_controls"]
            )
        )
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "rule_config" in value:
        import aws_sdk_route53_recovery_control_config.types.rule_config

        out["RuleConfig"] = (
            aws_sdk_route53_recovery_control_config.types.rule_config.serialize_json(
                value["rule_config"]
            )
        )
    if "safety_rule_arn" in value:
        out["SafetyRuleArn"] = value["safety_rule_arn"]
    if "status" in value:
        import aws_sdk_route53_recovery_control_config.types.status

        out["Status"] = (
            aws_sdk_route53_recovery_control_config.types.status.serialize_json(
                value["status"]
            )
        )
    if "wait_period_ms" in value:
        out["WaitPeriodMs"] = value["wait_period_ms"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_json(data: dict) -> AssertionRule:
    out: AssertionRule = {}  # type: ignore[typeddict-item]
    if "AssertedControls" in data:
        import aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["asserted_controls"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.deserialize_json(
                data["AssertedControls"]
            )
        )
    if "ControlPanelArn" in data:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RuleConfig" in data:
        import aws_sdk_route53_recovery_control_config.types.rule_config

        out["rule_config"] = (
            aws_sdk_route53_recovery_control_config.types.rule_config.deserialize_json(
                data["RuleConfig"]
            )
        )
    if "SafetyRuleArn" in data:
        out["safety_rule_arn"] = data["SafetyRuleArn"]
    if "Status" in data:
        import aws_sdk_route53_recovery_control_config.types.status

        out["status"] = (
            aws_sdk_route53_recovery_control_config.types.status.deserialize_json(
                data["Status"]
            )
        )
    if "WaitPeriodMs" in data:
        out["wait_period_ms"] = data["WaitPeriodMs"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    return out
