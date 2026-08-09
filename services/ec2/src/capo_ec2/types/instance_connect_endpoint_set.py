"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceConnectEndpointSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ec2_instance_connect_endpoint

InstanceConnectEndpointSet: TypeAlias = list[
    "capo_ec2.types.ec2_instance_connect_endpoint.Ec2InstanceConnectEndpoint"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceConnectEndpointSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ec2_instance_connect_endpoint

        capo_ec2.types.ec2_instance_connect_endpoint.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceConnectEndpointSet:
    import capo_ec2.types.ec2_instance_connect_endpoint

    out: InstanceConnectEndpointSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ec2_instance_connect_endpoint.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceConnectEndpointSet:
    import capo_ec2.types.ec2_instance_connect_endpoint

    out: InstanceConnectEndpointSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ec2_instance_connect_endpoint.deserialize_ec2_query(child)
        )
    return out
