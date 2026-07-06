"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateClientVpnTargetNetworkResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.association_status
    import aws_sdk_ec2.types.string


class DisassociateClientVpnTargetNetworkResult(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the target network association.</p>"""
    status: NotRequired["aws_sdk_ec2.types.association_status.AssociationStatus"]
    """<p>The current state of the target network association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateClientVpnTargetNetworkResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))
    if "status" in value:
        import aws_sdk_ec2.types.association_status

        aws_sdk_ec2.types.association_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_ec2_query(el: Element) -> DisassociateClientVpnTargetNetworkResult:
    out: DisassociateClientVpnTargetNetworkResult = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.association_status

        out["status"] = aws_sdk_ec2.types.association_status.deserialize_ec2_query(
            child_status
        )
    return out
