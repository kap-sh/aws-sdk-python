"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConcentratorList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_concentrator

VpnConcentratorList: TypeAlias = list["capo_ec2.types.vpn_concentrator.VpnConcentrator"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConcentratorList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpn_concentrator

        capo_ec2.types.vpn_concentrator.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VpnConcentratorList:
    import capo_ec2.types.vpn_concentrator

    out: VpnConcentratorList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpn_concentrator.deserialize_ec2_query(child))
    return out
