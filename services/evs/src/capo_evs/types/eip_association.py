"""Generated from Smithy shape ``com.amazonaws.evs#EipAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.allocation_id
    import capo_evs.types.association_id
    import capo_evs.types.ip_address


class EipAssociation(TypedDict, closed=True):
    association_id: NotRequired["capo_evs.types.association_id.AssociationId"]
    """<p>A unique ID for the elastic IP address association with the VLAN subnet.</p>"""
    allocation_id: NotRequired["capo_evs.types.allocation_id.AllocationId"]
    """<p>The Elastic IP address allocation ID.</p>"""
    ip_address: NotRequired["capo_evs.types.ip_address.IpAddress"]
    """<p>The Elastic IP address.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EipAssociation) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "allocation_id" in value:
        out["allocationId"] = value["allocation_id"]
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EipAssociation:
    out: EipAssociation = {}  # type: ignore[typeddict-item]
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    if "allocationId" in data:
        out["allocation_id"] = data["allocationId"]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    return out
