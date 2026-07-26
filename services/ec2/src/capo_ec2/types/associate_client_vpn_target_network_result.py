"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateClientVpnTargetNetworkResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.association_status
    import capo_ec2.types.string


class AssociateClientVpnTargetNetworkResult(TypedDict, closed=True):
    association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The unique ID of the target network association.</p>"""
    status: NotRequired["capo_ec2.types.association_status.AssociationStatus"]
    """<p>The current state of the target network association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateClientVpnTargetNetworkResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "status" in value:
        import capo_ec2.types.association_status

        capo_ec2.types.association_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> AssociateClientVpnTargetNetworkResult:
    out: AssociateClientVpnTargetNetworkResult = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.association_status

        out["status"] = capo_ec2.types.association_status.deserialize_ec2_query(
            child_status
        )
    return out
