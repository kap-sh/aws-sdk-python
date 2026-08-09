"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_endpoint

VpcEndpointSet: TypeAlias = list["capo_ec2.types.vpc_endpoint.VpcEndpoint"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEndpointSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpc_endpoint

        capo_ec2.types.vpc_endpoint.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> VpcEndpointSet:
    import capo_ec2.types.vpc_endpoint

    out: VpcEndpointSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.vpc_endpoint.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VpcEndpointSet:
    import capo_ec2.types.vpc_endpoint

    out: VpcEndpointSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpc_endpoint.deserialize_ec2_query(child))
    return out
