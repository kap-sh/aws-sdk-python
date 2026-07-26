"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateVpcCidrBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_cidr_association_id


class DisassociateVpcCidrBlockRequest(TypedDict, closed=True):
    association_id: NotRequired[
        "capo_ec2.types.vpc_cidr_association_id.VpcCidrAssociationId"
    ]
    """<p>The association ID for the CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateVpcCidrBlockRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))


def deserialize_ec2_query(el: Element) -> DisassociateVpcCidrBlockRequest:
    out: DisassociateVpcCidrBlockRequest = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    return out
