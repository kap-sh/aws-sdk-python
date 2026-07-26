"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayRegistrationStateReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.transit_gateway_registration_state


class TransitGatewayRegistrationStateReason(TypedDict, closed=True):
    code: NotRequired[
        "capo_networkmanager.types.transit_gateway_registration_state.TransitGatewayRegistrationState"
    ]
    """<p>The code for the state reason.</p>"""
    message: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The message for the state reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayRegistrationStateReason) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_networkmanager.types.transit_gateway_registration_state

        out["Code"] = (
            capo_networkmanager.types.transit_gateway_registration_state.serialize_json(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TransitGatewayRegistrationStateReason:
    out: TransitGatewayRegistrationStateReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_networkmanager.types.transit_gateway_registration_state

        out["code"] = (
            capo_networkmanager.types.transit_gateway_registration_state.deserialize_json(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
