"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#Rule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.assertion_rule
    import aws_sdk_route53_recovery_control_config.types.gating_rule


class Rule(TypedDict):
    assertion: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.assertion_rule.AssertionRule"
    ]
    """<p>An assertion rule enforces that, when a routing control state is changed, the criteria set by the rule configuration is met. Otherwise, the change to the routing control state is not accepted. For example, the criteria might be that at least one routing control state is On after the transaction so that traffic continues to flow to at least one cell for the application. This ensures that you avoid a fail-open scenario.</p>"""
    gating: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.gating_rule.GatingRule"
    ]
    r"""<p>A gating rule verifies that a gating routing control or set of gating routing controls, evaluates as true, based on a rule configuration that you specify, which allows a set of routing control state changes to complete.</p> <p>For example, if you specify one gating routing control and you set the Type in the rule configuration to OR, that indicates that you must set the gating routing control to On for the rule to evaluate as true; that is, for the gating control \"switch\" to be \"On\". When you do that, then you can update the routing control states for the target routing controls that you specify in the gating rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    if "assertion" in value:
        import aws_sdk_route53_recovery_control_config.types.assertion_rule

        out["ASSERTION"] = (
            aws_sdk_route53_recovery_control_config.types.assertion_rule.serialize_json(
                value["assertion"]
            )
        )
    if "gating" in value:
        import aws_sdk_route53_recovery_control_config.types.gating_rule

        out["GATING"] = (
            aws_sdk_route53_recovery_control_config.types.gating_rule.serialize_json(
                value["gating"]
            )
        )
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "ASSERTION" in data:
        import aws_sdk_route53_recovery_control_config.types.assertion_rule

        out["assertion"] = (
            aws_sdk_route53_recovery_control_config.types.assertion_rule.deserialize_json(
                data["ASSERTION"]
            )
        )
    if "GATING" in data:
        import aws_sdk_route53_recovery_control_config.types.gating_rule

        out["gating"] = (
            aws_sdk_route53_recovery_control_config.types.gating_rule.deserialize_json(
                data["GATING"]
            )
        )
    return out
