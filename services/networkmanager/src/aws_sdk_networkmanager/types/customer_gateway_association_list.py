"""Generated from Smithy shape ``com.amazonaws.networkmanager#CustomerGatewayAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.customer_gateway_association

CustomerGatewayAssociationList: TypeAlias = list[
    "aws_sdk_networkmanager.types.customer_gateway_association.CustomerGatewayAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerGatewayAssociationList) -> list:
    import aws_sdk_networkmanager.types.customer_gateway_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.customer_gateway_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CustomerGatewayAssociationList:
    import aws_sdk_networkmanager.types.customer_gateway_association

    out: CustomerGatewayAssociationList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.customer_gateway_association.deserialize_json(
                item
            )
        )
    return out
