"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateSubnetCidrBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.subnet_cidr_association_id


class DisassociateSubnetCidrBlockRequest(TypedDict, closed=True):
    association_id: NotRequired[
        "capo_ec2.types.subnet_cidr_association_id.SubnetCidrAssociationId"
    ]
    """<p>The association ID for the CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateSubnetCidrBlockRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association_id" in value:
        pairs.append((f"{key_prefix}AssociationId", str(value["association_id"])))


def deserialize_ec2_query(el: Element) -> DisassociateSubnetCidrBlockRequest:
    out: DisassociateSubnetCidrBlockRequest = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("associationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    return out
