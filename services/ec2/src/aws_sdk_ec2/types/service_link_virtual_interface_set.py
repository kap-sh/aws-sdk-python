"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceLinkVirtualInterfaceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_link_virtual_interface

ServiceLinkVirtualInterfaceSet: TypeAlias = list[
    "aws_sdk_ec2.types.service_link_virtual_interface.ServiceLinkVirtualInterface"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceLinkVirtualInterfaceSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.service_link_virtual_interface

        aws_sdk_ec2.types.service_link_virtual_interface.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ServiceLinkVirtualInterfaceSet:
    import aws_sdk_ec2.types.service_link_virtual_interface

    out: ServiceLinkVirtualInterfaceSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.service_link_virtual_interface.deserialize_ec2_query(
                child
            )
        )
    return out
