"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#__listOfRule``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.rule

__listOfRule: TypeAlias = list["capo_route53_recovery_control_config.types.rule.Rule"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRule) -> list:
    import capo_route53_recovery_control_config.types.rule

    out: list = []
    for item in value:
        out.append(capo_route53_recovery_control_config.types.rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRule:
    import capo_route53_recovery_control_config.types.rule

    out: __listOfRule = []
    for item in data:
        out.append(
            capo_route53_recovery_control_config.types.rule.deserialize_json(item)
        )
    return out
