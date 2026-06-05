"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceSecondaryInterfaceSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification

LaunchTemplateInstanceSecondaryInterfaceSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification.LaunchTemplateInstanceSecondaryInterfaceSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateInstanceSecondaryInterfaceSpecificationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification

        aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> LaunchTemplateInstanceSecondaryInterfaceSpecificationList:
    import aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification

    out: LaunchTemplateInstanceSecondaryInterfaceSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification.deserialize_ec2_query(
                child
            )
        )
    return out
