"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeregisterTransitGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.transit_gateway_registration


class DeregisterTransitGatewayResponse(TypedDict, closed=True):
    transit_gateway_registration: NotRequired[
        "capo_networkmanager.types.transit_gateway_registration.TransitGatewayRegistration"
    ]
    """<p>The transit gateway registration information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterTransitGatewayResponse) -> dict:
    out: dict = {}
    if "transit_gateway_registration" in value:
        import capo_networkmanager.types.transit_gateway_registration

        out["TransitGatewayRegistration"] = (
            capo_networkmanager.types.transit_gateway_registration.serialize_json(
                value["transit_gateway_registration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeregisterTransitGatewayResponse:
    out: DeregisterTransitGatewayResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayRegistration" in data:
        import capo_networkmanager.types.transit_gateway_registration

        out["transit_gateway_registration"] = (
            capo_networkmanager.types.transit_gateway_registration.deserialize_json(
                data["TransitGatewayRegistration"]
            )
        )
    return out
