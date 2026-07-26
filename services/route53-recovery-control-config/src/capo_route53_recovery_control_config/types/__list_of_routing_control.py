"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#__listOfRoutingControl``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.routing_control

__listOfRoutingControl: TypeAlias = list[
    "capo_route53_recovery_control_config.types.routing_control.RoutingControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRoutingControl) -> list:
    import capo_route53_recovery_control_config.types.routing_control

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_control_config.types.routing_control.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfRoutingControl:
    import capo_route53_recovery_control_config.types.routing_control

    out: __listOfRoutingControl = []
    for item in data:
        out.append(
            capo_route53_recovery_control_config.types.routing_control.deserialize_json(
                item
            )
        )
    return out
