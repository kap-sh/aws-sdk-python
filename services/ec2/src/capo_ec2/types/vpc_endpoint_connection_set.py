"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointConnectionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_endpoint_connection

VpcEndpointConnectionSet: TypeAlias = list[
    "capo_ec2.types.vpc_endpoint_connection.VpcEndpointConnection"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEndpointConnectionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpc_endpoint_connection

        capo_ec2.types.vpc_endpoint_connection.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VpcEndpointConnectionSet:
    import capo_ec2.types.vpc_endpoint_connection

    out: VpcEndpointConnectionSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.vpc_endpoint_connection.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VpcEndpointConnectionSet:
    import capo_ec2.types.vpc_endpoint_connection

    out: VpcEndpointConnectionSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpc_endpoint_connection.deserialize_ec2_query(child))
    return out
