"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentBgpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_attachment_bgp_configuration

TransitGatewayAttachmentBgpConfigurationList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_attachment_bgp_configuration.TransitGatewayAttachmentBgpConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachmentBgpConfigurationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_attachment_bgp_configuration

        capo_ec2.types.transit_gateway_attachment_bgp_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentBgpConfigurationList:
    import capo_ec2.types.transit_gateway_attachment_bgp_configuration

    out: TransitGatewayAttachmentBgpConfigurationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_attachment_bgp_configuration.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayAttachmentBgpConfigurationList:
    import capo_ec2.types.transit_gateway_attachment_bgp_configuration

    out: TransitGatewayAttachmentBgpConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_attachment_bgp_configuration.deserialize_ec2_query(
                child
            )
        )
    return out
