"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_peering_connection

VpcPeeringConnectionList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_peering_connection.VpcPeeringConnection"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcPeeringConnectionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.vpc_peering_connection

        aws_sdk_ec2.types.vpc_peering_connection.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VpcPeeringConnectionList:
    import aws_sdk_ec2.types.vpc_peering_connection

    out: VpcPeeringConnectionList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.vpc_peering_connection.deserialize_ec2_query(child)
        )
    return out
