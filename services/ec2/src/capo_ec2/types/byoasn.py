"""Generated from Smithy shape ``com.amazonaws.ec2#Byoasn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.asn_state
    import capo_ec2.types.ipam_id
    import capo_ec2.types.string


class Byoasn(TypedDict, closed=True):
    asn: NotRequired["capo_ec2.types.string.String"]
    """<p>A public 2-byte or 4-byte ASN.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>An IPAM ID.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The status message.</p>"""
    state: NotRequired["capo_ec2.types.asn_state.AsnState"]
    """<p>The provisioning state of the BYOASN.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Byoasn, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "asn" in value:
        pairs.append((f"{prefix}.Asn", str(value["asn"])))
    if "ipam_id" in value:
        pairs.append((f"{prefix}.IpamId", str(value["ipam_id"])))
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "state" in value:
        import capo_ec2.types.asn_state

        capo_ec2.types.asn_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> Byoasn:
    out: Byoasn = {}  # type: ignore[typeddict-item]
    child_asn = el.find("Asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.asn_state

        out["state"] = capo_ec2.types.asn_state.deserialize_ec2_query(child_state)
    return out
