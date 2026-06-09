"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPrefixListReferenceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference

TransitGatewayPrefixListReferenceSet: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_prefix_list_reference.TransitGatewayPrefixListReference"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPrefixListReferenceSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_prefix_list_reference

        aws_sdk_ec2.types.transit_gateway_prefix_list_reference.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayPrefixListReferenceSet:
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference

    out: TransitGatewayPrefixListReferenceSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_prefix_list_reference.deserialize_ec2_query(
                child
            )
        )
    return out
