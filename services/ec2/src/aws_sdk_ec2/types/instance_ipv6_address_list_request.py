"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6AddressListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_ipv6_address_request

InstanceIpv6AddressListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.instance_ipv6_address_request.InstanceIpv6AddressRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv6AddressListRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_ipv6_address_request

        aws_sdk_ec2.types.instance_ipv6_address_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceIpv6AddressListRequest:
    import aws_sdk_ec2.types.instance_ipv6_address_request

    out: InstanceIpv6AddressListRequest = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.instance_ipv6_address_request.deserialize_ec2_query(child)
        )
    return out
