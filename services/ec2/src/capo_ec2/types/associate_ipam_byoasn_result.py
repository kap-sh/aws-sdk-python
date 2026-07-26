"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIpamByoasnResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.asn_association


class AssociateIpamByoasnResult(TypedDict, closed=True):
    asn_association: NotRequired["capo_ec2.types.asn_association.AsnAssociation"]
    """<p>The ASN and BYOIP CIDR association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateIpamByoasnResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "asn_association" in value:
        import capo_ec2.types.asn_association

        capo_ec2.types.asn_association.serialize_ec2_query(
            value["asn_association"], pairs, f"{prefix}.AsnAssociation"
        )


def deserialize_ec2_query(el: Element) -> AssociateIpamByoasnResult:
    out: AssociateIpamByoasnResult = {}  # type: ignore[typeddict-item]
    child_asn_association = el.find("AsnAssociation")
    if child_asn_association is not None:
        import capo_ec2.types.asn_association

        out["asn_association"] = capo_ec2.types.asn_association.deserialize_ec2_query(
            child_asn_association
        )
    return out
