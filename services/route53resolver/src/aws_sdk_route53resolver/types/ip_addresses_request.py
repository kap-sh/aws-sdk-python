"""Generated from Smithy shape ``com.amazonaws.route53resolver#IpAddressesRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.ip_address_request

IpAddressesRequest: TypeAlias = list[
    "aws_sdk_route53resolver.types.ip_address_request.IpAddressRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressesRequest) -> list:
    import aws_sdk_route53resolver.types.ip_address_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.ip_address_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IpAddressesRequest:
    import aws_sdk_route53resolver.types.ip_address_request

    out: IpAddressesRequest = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.ip_address_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
