"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressesRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.ip_address_request

IpAddressesRequest: TypeAlias = list[
    "capo_route53resolver.types.ip_address_request.IpAddressRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressesRequest) -> list:
    import capo_route53resolver.types.ip_address_request

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.ip_address_request.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IpAddressesRequest:
    import capo_route53resolver.types.ip_address_request

    out: IpAddressesRequest = []
    for item in data:
        out.append(
            capo_route53resolver.types.ip_address_request.deserialize_aws_json_1_1(item)
        )
    return out
