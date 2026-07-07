"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayRegistrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.next_token
    import aws_sdk_networkmanager.types.transit_gateway_registration_list


class GetTransitGatewayRegistrationsResponse(TypedDict, closed=True):
    transit_gateway_registrations: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_registration_list.TransitGatewayRegistrationList"
    ]
    """<p>The transit gateway registrations.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayRegistrationsResponse) -> dict:
    out: dict = {}
    if "transit_gateway_registrations" in value:
        import aws_sdk_networkmanager.types.transit_gateway_registration_list

        out["TransitGatewayRegistrations"] = (
            aws_sdk_networkmanager.types.transit_gateway_registration_list.serialize_json(
                value["transit_gateway_registrations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTransitGatewayRegistrationsResponse:
    out: GetTransitGatewayRegistrationsResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayRegistrations" in data:
        import aws_sdk_networkmanager.types.transit_gateway_registration_list

        out["transit_gateway_registrations"] = (
            aws_sdk_networkmanager.types.transit_gateway_registration_list.deserialize_json(
                data["TransitGatewayRegistrations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
