"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateIpAddressConfigSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.scheduled_instances_private_ip_address_config

PrivateIpAddressConfigSet: TypeAlias = list[
    "capo_ec2.types.scheduled_instances_private_ip_address_config.ScheduledInstancesPrivateIpAddressConfig"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateIpAddressConfigSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.scheduled_instances_private_ip_address_config

        capo_ec2.types.scheduled_instances_private_ip_address_config.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PrivateIpAddressConfigSet:
    import capo_ec2.types.scheduled_instances_private_ip_address_config

    out: PrivateIpAddressConfigSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.scheduled_instances_private_ip_address_config.deserialize_ec2_query(
                child
            )
        )
    return out
