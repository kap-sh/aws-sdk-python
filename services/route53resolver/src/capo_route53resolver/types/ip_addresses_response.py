"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressesResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.ip_address_response

IpAddressesResponse: TypeAlias = list[
    "capo_route53resolver.types.ip_address_response.IpAddressResponse"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressesResponse) -> list:
    import capo_route53resolver.types.ip_address_response

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.ip_address_response.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IpAddressesResponse:
    import capo_route53resolver.types.ip_address_response

    out: IpAddressesResponse = []
    for item in data:
        out.append(
            capo_route53resolver.types.ip_address_response.deserialize_aws_json_1_1(
                item
            )
        )
    return out
