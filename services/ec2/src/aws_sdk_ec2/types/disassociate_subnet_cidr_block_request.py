"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateSubnetCidrBlockRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_cidr_association_id


class DisassociateSubnetCidrBlockRequest(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_association_id.SubnetCidrAssociationId"
    ]
    """<p>The association ID for the CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateSubnetCidrBlockRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))


def deserialize_ec2_query(el: Element) -> DisassociateSubnetCidrBlockRequest:
    out: DisassociateSubnetCidrBlockRequest = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    return out
