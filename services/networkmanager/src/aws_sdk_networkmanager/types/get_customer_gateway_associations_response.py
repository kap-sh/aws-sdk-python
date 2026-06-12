"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetCustomerGatewayAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.customer_gateway_association_list
    import aws_sdk_networkmanager.types.next_token


class GetCustomerGatewayAssociationsResponse(TypedDict):
    customer_gateway_associations: NotRequired[
        "aws_sdk_networkmanager.types.customer_gateway_association_list.CustomerGatewayAssociationList"
    ]
    """<p>The customer gateway associations.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomerGatewayAssociationsResponse) -> dict:
    out: dict = {}
    if "customer_gateway_associations" in value:
        import aws_sdk_networkmanager.types.customer_gateway_association_list

        out["CustomerGatewayAssociations"] = (
            aws_sdk_networkmanager.types.customer_gateway_association_list.serialize_json(
                value["customer_gateway_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCustomerGatewayAssociationsResponse:
    out: GetCustomerGatewayAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "CustomerGatewayAssociations" in data:
        import aws_sdk_networkmanager.types.customer_gateway_association_list

        out["customer_gateway_associations"] = (
            aws_sdk_networkmanager.types.customer_gateway_association_list.deserialize_json(
                data["CustomerGatewayAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
