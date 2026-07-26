"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#RuleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__boolean
    import capo_route53_recovery_control_config.types.__integer
    import capo_route53_recovery_control_config.types.rule_type


class RuleConfig(TypedDict, closed=True):
    inverted: NotRequired[
        "capo_route53_recovery_control_config.types.__boolean.__boolean"
    ]
    """<p>Logical negation of the rule. If the rule would usually evaluate true, it's evaluated as false, and vice versa.</p>"""
    threshold: NotRequired[
        "capo_route53_recovery_control_config.types.__integer.__integer"
    ]
    """<p>The value of N, when you specify an ATLEAST rule type. That is, Threshold is the number of controls that must be set when you specify an ATLEAST type.</p>"""
    type: NotRequired["capo_route53_recovery_control_config.types.rule_type.RuleType"]
    """<p>A rule can be one of the following: ATLEAST, AND, or OR.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleConfig) -> dict:
    out: dict = {}
    if "inverted" in value:
        out["Inverted"] = value["inverted"]
    if "threshold" in value:
        out["Threshold"] = value["threshold"]
    if "type" in value:
        import capo_route53_recovery_control_config.types.rule_type

        out["Type"] = (
            capo_route53_recovery_control_config.types.rule_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleConfig:
    out: RuleConfig = {}  # type: ignore[typeddict-item]
    if "Inverted" in data:
        out["inverted"] = data["Inverted"]
    if "Threshold" in data:
        out["threshold"] = data["Threshold"]
    if "Type" in data:
        import capo_route53_recovery_control_config.types.rule_type

        out["type"] = (
            capo_route53_recovery_control_config.types.rule_type.deserialize_json(
                data["Type"]
            )
        )
    return out
