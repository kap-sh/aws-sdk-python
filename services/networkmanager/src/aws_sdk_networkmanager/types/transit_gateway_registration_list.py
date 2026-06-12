"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayRegistrationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.transit_gateway_registration

TransitGatewayRegistrationList: TypeAlias = list[
    "aws_sdk_networkmanager.types.transit_gateway_registration.TransitGatewayRegistration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayRegistrationList) -> list:
    import aws_sdk_networkmanager.types.transit_gateway_registration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.transit_gateway_registration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TransitGatewayRegistrationList:
    import aws_sdk_networkmanager.types.transit_gateway_registration

    out: TransitGatewayRegistrationList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.transit_gateway_registration.deserialize_json(
                item
            )
        )
    return out
