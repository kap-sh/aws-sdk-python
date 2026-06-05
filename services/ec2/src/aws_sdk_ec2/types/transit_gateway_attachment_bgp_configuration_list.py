"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentBgpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration

TransitGatewayAttachmentBgpConfigurationList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration.TransitGatewayAttachmentBgpConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachmentBgpConfigurationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration

        aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayAttachmentBgpConfigurationList:
    import aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration

    out: TransitGatewayAttachmentBgpConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration.deserialize_ec2_query(
                child
            )
        )
    return out
