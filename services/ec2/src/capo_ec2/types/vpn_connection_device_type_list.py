"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionDeviceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_connection_device_type

VpnConnectionDeviceTypeList: TypeAlias = list[
    "capo_ec2.types.vpn_connection_device_type.VpnConnectionDeviceType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConnectionDeviceTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpn_connection_device_type

        capo_ec2.types.vpn_connection_device_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VpnConnectionDeviceTypeList:
    import capo_ec2.types.vpn_connection_device_type

    out: VpnConnectionDeviceTypeList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.vpn_connection_device_type.deserialize_ec2_query(child)
        )
    return out
