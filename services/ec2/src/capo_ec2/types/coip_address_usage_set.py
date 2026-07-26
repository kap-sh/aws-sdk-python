"""Generated from Smithy shape ``com.amazonaws.ec2#CoipAddressUsageSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.coip_address_usage

CoipAddressUsageSet: TypeAlias = list[
    "capo_ec2.types.coip_address_usage.CoipAddressUsage"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CoipAddressUsageSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.coip_address_usage

        capo_ec2.types.coip_address_usage.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CoipAddressUsageSet:
    import capo_ec2.types.coip_address_usage

    out: CoipAddressUsageSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.coip_address_usage.deserialize_ec2_query(child))
    return out
