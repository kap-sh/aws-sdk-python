"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_network_interface_specification

InstanceNetworkInterfaceSpecificationList: TypeAlias = list[
    "capo_ec2.types.instance_network_interface_specification.InstanceNetworkInterfaceSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceNetworkInterfaceSpecificationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_network_interface_specification

        capo_ec2.types.instance_network_interface_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceNetworkInterfaceSpecificationList:
    import capo_ec2.types.instance_network_interface_specification

    out: InstanceNetworkInterfaceSpecificationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.instance_network_interface_specification.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> InstanceNetworkInterfaceSpecificationList:
    import capo_ec2.types.instance_network_interface_specification

    out: InstanceNetworkInterfaceSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.instance_network_interface_specification.deserialize_ec2_query(
                child
            )
        )
    return out
