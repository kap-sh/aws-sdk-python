"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetCustomerGatewayAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.customer_gateway_association_list
    import capo_networkmanager.types.next_token


class GetCustomerGatewayAssociationsResponse(TypedDict, closed=True):
    customer_gateway_associations: NotRequired[
        "capo_networkmanager.types.customer_gateway_association_list.CustomerGatewayAssociationList"
    ]
    """<p>The customer gateway associations.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomerGatewayAssociationsResponse) -> dict:
    out: dict = {}
    if "customer_gateway_associations" in value:
        import capo_networkmanager.types.customer_gateway_association_list

        out["CustomerGatewayAssociations"] = (
            capo_networkmanager.types.customer_gateway_association_list.serialize_json(
                value["customer_gateway_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCustomerGatewayAssociationsResponse:
    out: GetCustomerGatewayAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "CustomerGatewayAssociations" in data:
        import capo_networkmanager.types.customer_gateway_association_list

        out["customer_gateway_associations"] = (
            capo_networkmanager.types.customer_gateway_association_list.deserialize_json(
                data["CustomerGatewayAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
