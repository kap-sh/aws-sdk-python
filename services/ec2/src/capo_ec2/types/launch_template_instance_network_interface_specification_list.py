"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceNetworkInterfaceSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_instance_network_interface_specification

LaunchTemplateInstanceNetworkInterfaceSpecificationList: TypeAlias = list[
    "capo_ec2.types.launch_template_instance_network_interface_specification.LaunchTemplateInstanceNetworkInterfaceSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceNetworkInterfaceSpecificationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_template_instance_network_interface_specification

        capo_ec2.types.launch_template_instance_network_interface_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> LaunchTemplateInstanceNetworkInterfaceSpecificationList:
    import capo_ec2.types.launch_template_instance_network_interface_specification

    out: LaunchTemplateInstanceNetworkInterfaceSpecificationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.launch_template_instance_network_interface_specification.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LaunchTemplateInstanceNetworkInterfaceSpecificationList:
    import capo_ec2.types.launch_template_instance_network_interface_specification

    out: LaunchTemplateInstanceNetworkInterfaceSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.launch_template_instance_network_interface_specification.deserialize_ec2_query(
                child
            )
        )
    return out
