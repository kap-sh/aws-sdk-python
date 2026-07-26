"""Generated from Smithy shape ``com.amazonaws.networkmanager#CustomerGatewayAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.customer_gateway_association

CustomerGatewayAssociationList: TypeAlias = list[
    "capo_networkmanager.types.customer_gateway_association.CustomerGatewayAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerGatewayAssociationList) -> list:
    import capo_networkmanager.types.customer_gateway_association

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.customer_gateway_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CustomerGatewayAssociationList:
    import capo_networkmanager.types.customer_gateway_association

    out: CustomerGatewayAssociationList = []
    for item in data:
        out.append(
            capo_networkmanager.types.customer_gateway_association.deserialize_json(
                item
            )
        )
    return out
