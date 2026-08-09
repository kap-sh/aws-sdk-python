"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_instance_network_interface_specification_request

LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList: TypeAlias = list[
    "capo_ec2.types.launch_template_instance_network_interface_specification_request.LaunchTemplateInstanceNetworkInterfaceSpecificationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_template_instance_network_interface_specification_request

        capo_ec2.types.launch_template_instance_network_interface_specification_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList:
    import capo_ec2.types.launch_template_instance_network_interface_specification_request

    out: LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList = []
    for child in el.findall("InstanceNetworkInterfaceSpecification"):
        out.append(
            capo_ec2.types.launch_template_instance_network_interface_specification_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList:
    import capo_ec2.types.launch_template_instance_network_interface_specification_request

    out: LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.launch_template_instance_network_interface_specification_request.deserialize_ec2_query(
                child
            )
        )
    return out
