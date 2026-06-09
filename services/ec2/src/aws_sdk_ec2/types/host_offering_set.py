"""Generated from Smithy shape ``com.amazonaws.ec2#HostOfferingSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host_offering

HostOfferingSet: TypeAlias = list["aws_sdk_ec2.types.host_offering.HostOffering"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HostOfferingSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.host_offering

        aws_sdk_ec2.types.host_offering.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> HostOfferingSet:
    import aws_sdk_ec2.types.host_offering

    out: HostOfferingSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.host_offering.deserialize_ec2_query(child))
    return out
