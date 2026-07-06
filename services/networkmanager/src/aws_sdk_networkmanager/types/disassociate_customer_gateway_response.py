"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateCustomerGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.customer_gateway_association


class DisassociateCustomerGatewayResponse(TypedDict, closed=True):
    customer_gateway_association: NotRequired[
        "aws_sdk_networkmanager.types.customer_gateway_association.CustomerGatewayAssociation"
    ]
    """<p>Information about the customer gateway association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateCustomerGatewayResponse) -> dict:
    out: dict = {}
    if "customer_gateway_association" in value:
        import aws_sdk_networkmanager.types.customer_gateway_association

        out["CustomerGatewayAssociation"] = (
            aws_sdk_networkmanager.types.customer_gateway_association.serialize_json(
                value["customer_gateway_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateCustomerGatewayResponse:
    out: DisassociateCustomerGatewayResponse = {}  # type: ignore[typeddict-item]
    if "CustomerGatewayAssociation" in data:
        import aws_sdk_networkmanager.types.customer_gateway_association

        out["customer_gateway_association"] = (
            aws_sdk_networkmanager.types.customer_gateway_association.deserialize_json(
                data["CustomerGatewayAssociation"]
            )
        )
    return out
