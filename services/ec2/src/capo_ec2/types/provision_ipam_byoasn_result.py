"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionIpamByoasnResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.byoasn


class ProvisionIpamByoasnResult(TypedDict, closed=True):
    byoasn: NotRequired["capo_ec2.types.byoasn.Byoasn"]
    """<p>An ASN and BYOIP CIDR association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProvisionIpamByoasnResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "byoasn" in value:
        import capo_ec2.types.byoasn

        capo_ec2.types.byoasn.serialize_ec2_query(
            value["byoasn"], pairs, f"{prefix}.Byoasn"
        )


def deserialize_ec2_query(el: Element) -> ProvisionIpamByoasnResult:
    out: ProvisionIpamByoasnResult = {}  # type: ignore[typeddict-item]
    child_byoasn = el.find("Byoasn")
    if child_byoasn is not None:
        import capo_ec2.types.byoasn

        out["byoasn"] = capo_ec2.types.byoasn.deserialize_ec2_query(child_byoasn)
    return out
