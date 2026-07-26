"""Generated from Smithy shape ``com.amazonaws.ec2#AdvertiseByoipCidrResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.byoip_cidr


class AdvertiseByoipCidrResult(TypedDict, closed=True):
    byoip_cidr: NotRequired["capo_ec2.types.byoip_cidr.ByoipCidr"]
    """<p>Information about the address range.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AdvertiseByoipCidrResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "byoip_cidr" in value:
        import capo_ec2.types.byoip_cidr

        capo_ec2.types.byoip_cidr.serialize_ec2_query(
            value["byoip_cidr"], pairs, f"{prefix}.ByoipCidr"
        )


def deserialize_ec2_query(el: Element) -> AdvertiseByoipCidrResult:
    out: AdvertiseByoipCidrResult = {}  # type: ignore[typeddict-item]
    child_byoip_cidr = el.find("ByoipCidr")
    if child_byoip_cidr is not None:
        import capo_ec2.types.byoip_cidr

        out["byoip_cidr"] = capo_ec2.types.byoip_cidr.deserialize_ec2_query(
            child_byoip_cidr
        )
    return out
