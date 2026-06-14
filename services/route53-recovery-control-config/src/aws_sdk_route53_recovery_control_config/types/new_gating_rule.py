"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#NewGatingRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__integer
    import aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import aws_sdk_route53_recovery_control_config.types.rule_config


class NewGatingRule(TypedDict):
    control_panel_arn: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the control panel.</p>"""
    gating_controls: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.__listOf__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The gating controls for the new gating rule. That is, routing controls that are evaluated by the rule configuration that you specify.</p>"""
    name: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name for the new gating rule.</p>"""
    rule_config: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.rule_config.RuleConfig"
    ]
    """<p>The criteria that you set for specific gating controls (routing controls) that designate how many control states must be ON to allow you to change (set or unset) the target control states.</p>"""
    target_controls: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.__listOf__stringMin1Max256PatternAZaZ09"
    ]
    """<p>Routing controls that can only be set or unset if the specified RuleConfig evaluates to true for the specified GatingControls. For example, say you have three gating controls, one for each of three Amazon Web Services Regions. Now you specify ATLEAST 2 as your RuleConfig. With these settings, you can only change (set or unset) the routing controls that you have specified as TargetControls if that rule evaluates to true.</p> <p>In other words, your ability to change the routing controls that you have specified as TargetControls is gated by the rule that you set for the routing controls in GatingControls.</p>"""
    wait_period_ms: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__integer.__integer"
    ]
    r"""<p>An evaluation period, in milliseconds (ms), during which any request against the target routing controls will fail. This helps prevent \"flapping\" of state. The wait period is 5000 ms by default, but you can choose a custom value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NewGatingRule) -> dict:
    out: dict = {}
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "gating_controls" in value:
        import aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["GatingControls"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.serialize_json(
                value["gating_controls"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "rule_config" in value:
        import aws_sdk_route53_recovery_control_config.types.rule_config

        out["RuleConfig"] = (
            aws_sdk_route53_recovery_control_config.types.rule_config.serialize_json(
                value["rule_config"]
            )
        )
    if "target_controls" in value:
        import aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["TargetControls"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.serialize_json(
                value["target_controls"]
            )
        )
    if "wait_period_ms" in value:
        out["WaitPeriodMs"] = value["wait_period_ms"]
    return out


def deserialize_json(data: dict) -> NewGatingRule:
    out: NewGatingRule = {}  # type: ignore[typeddict-item]
    if "ControlPanelArn" in data:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if "GatingControls" in data:
        import aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["gating_controls"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.deserialize_json(
                data["GatingControls"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "RuleConfig" in data:
        import aws_sdk_route53_recovery_control_config.types.rule_config

        out["rule_config"] = (
            aws_sdk_route53_recovery_control_config.types.rule_config.deserialize_json(
                data["RuleConfig"]
            )
        )
    if "TargetControls" in data:
        import aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09

        out["target_controls"] = (
            aws_sdk_route53_recovery_control_config.types.__list_of__string_min1_max256_pattern_a_za_z09.deserialize_json(
                data["TargetControls"]
            )
        )
    if "WaitPeriodMs" in data:
        out["wait_period_ms"] = data["WaitPeriodMs"]
    return out
