"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListRoutingControlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__list_of_routing_control
    import capo_route53_recovery_control_config.types.__string_min1_max8096_pattern_s


class ListRoutingControlsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max8096_pattern_s.__stringMin1Max8096PatternS"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    routing_controls: NotRequired[
        "capo_route53_recovery_control_config.types.__list_of_routing_control.__listOfRoutingControl"
    ]
    """<p>An array of routing controls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutingControlsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "routing_controls" in value:
        import capo_route53_recovery_control_config.types.__list_of_routing_control

        out["RoutingControls"] = (
            capo_route53_recovery_control_config.types.__list_of_routing_control.serialize_json(
                value["routing_controls"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRoutingControlsResponse:
    out: ListRoutingControlsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RoutingControls" in data:
        import capo_route53_recovery_control_config.types.__list_of_routing_control

        out["routing_controls"] = (
            capo_route53_recovery_control_config.types.__list_of_routing_control.deserialize_json(
                data["RoutingControls"]
            )
        )
    return out
