"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_instance_secondary_interface_specification_request

LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList: TypeAlias = list[
    "capo_ec2.types.launch_template_instance_secondary_interface_specification_request.LaunchTemplateInstanceSecondaryInterfaceSpecificationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.launch_template_instance_secondary_interface_specification_request

        capo_ec2.types.launch_template_instance_secondary_interface_specification_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList:
    import capo_ec2.types.launch_template_instance_secondary_interface_specification_request

    out: LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList = []
    for child in el.findall("InstanceSecondaryInterfaceSpecification"):
        out.append(
            capo_ec2.types.launch_template_instance_secondary_interface_specification_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList:
    import capo_ec2.types.launch_template_instance_secondary_interface_specification_request

    out: LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.launch_template_instance_secondary_interface_specification_request.deserialize_ec2_query(
                child
            )
        )
    return out
