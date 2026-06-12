"""Generated from Smithy shape ``com.amazonaws.networkmanager#RegisterTransitGatewayResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.transit_gateway_registration


class RegisterTransitGatewayResponse(TypedDict):
    transit_gateway_registration: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_registration.TransitGatewayRegistration"
    ]
    """<p>Information about the transit gateway registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterTransitGatewayResponse) -> dict:
    out: dict = {}
    if "transit_gateway_registration" in value:
        import aws_sdk_networkmanager.types.transit_gateway_registration

        out["TransitGatewayRegistration"] = (
            aws_sdk_networkmanager.types.transit_gateway_registration.serialize_json(
                value["transit_gateway_registration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisterTransitGatewayResponse:
    out: RegisterTransitGatewayResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayRegistration" in data:
        import aws_sdk_networkmanager.types.transit_gateway_registration

        out["transit_gateway_registration"] = (
            aws_sdk_networkmanager.types.transit_gateway_registration.deserialize_json(
                data["TransitGatewayRegistration"]
            )
        )
    return out
