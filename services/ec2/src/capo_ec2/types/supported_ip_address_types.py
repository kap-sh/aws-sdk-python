"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedIpAddressTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.service_connectivity_type

SupportedIpAddressTypes: TypeAlias = list[
    "capo_ec2.types.service_connectivity_type.ServiceConnectivityType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SupportedIpAddressTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.service_connectivity_type

        capo_ec2.types.service_connectivity_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SupportedIpAddressTypes:
    import capo_ec2.types.service_connectivity_type

    out: SupportedIpAddressTypes = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.service_connectivity_type.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SupportedIpAddressTypes:
    import capo_ec2.types.service_connectivity_type

    out: SupportedIpAddressTypes = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.service_connectivity_type.deserialize_ec2_query(child)
        )
    return out
