"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateRoutingControlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.routing_control


class UpdateRoutingControlResponse(TypedDict, closed=True):
    routing_control: NotRequired[
        "capo_route53_recovery_control_config.types.routing_control.RoutingControl"
    ]
    """<p>The routing control that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingControlResponse) -> dict:
    out: dict = {}
    if "routing_control" in value:
        import capo_route53_recovery_control_config.types.routing_control

        out["RoutingControl"] = (
            capo_route53_recovery_control_config.types.routing_control.serialize_json(
                value["routing_control"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRoutingControlResponse:
    out: UpdateRoutingControlResponse = {}  # type: ignore[typeddict-item]
    if "RoutingControl" in data:
        import capo_route53_recovery_control_config.types.routing_control

        out["routing_control"] = (
            capo_route53_recovery_control_config.types.routing_control.deserialize_json(
                data["RoutingControl"]
            )
        )
    return out
