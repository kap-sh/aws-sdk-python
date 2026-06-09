"""Generated from Smithy shape ``com.amazonaws.ec2#EndpointSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint

EndpointSet: TypeAlias = list["aws_sdk_ec2.types.client_vpn_endpoint.ClientVpnEndpoint"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EndpointSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.client_vpn_endpoint

        aws_sdk_ec2.types.client_vpn_endpoint.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> EndpointSet:
    import aws_sdk_ec2.types.client_vpn_endpoint

    out: EndpointSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.client_vpn_endpoint.deserialize_ec2_query(child))
    return out
