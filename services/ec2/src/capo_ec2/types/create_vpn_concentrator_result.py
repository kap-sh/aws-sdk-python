"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnConcentratorResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_concentrator


class CreateVpnConcentratorResult(TypedDict, closed=True):
    vpn_concentrator: NotRequired["capo_ec2.types.vpn_concentrator.VpnConcentrator"]
    """<p>Information about the VPN concentrator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpnConcentratorResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_concentrator" in value:
        import capo_ec2.types.vpn_concentrator

        capo_ec2.types.vpn_concentrator.serialize_ec2_query(
            value["vpn_concentrator"], pairs, f"{prefix}.VpnConcentrator"
        )


def deserialize_ec2_query(el: Element) -> CreateVpnConcentratorResult:
    out: CreateVpnConcentratorResult = {}  # type: ignore[typeddict-item]
    child_vpn_concentrator = el.find("VpnConcentrator")
    if child_vpn_concentrator is not None:
        import capo_ec2.types.vpn_concentrator

        out["vpn_concentrator"] = capo_ec2.types.vpn_concentrator.deserialize_ec2_query(
            child_vpn_concentrator
        )
    return out
