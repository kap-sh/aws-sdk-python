"""Generated from Smithy shape ``com.amazonaws.ec2#AsnAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_association_state
    import aws_sdk_ec2.types.string


class AsnAssociation(TypedDict):
    asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association's ASN.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association's CIDR.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association's status message.</p>"""
    state: NotRequired["aws_sdk_ec2.types.asn_association_state.AsnAssociationState"]
    """<p>The association's state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AsnAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "asn" in value:
        pairs.append((f"{prefix}.Asn", str(value["asn"])))
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "state" in value:
        import aws_sdk_ec2.types.asn_association_state

        aws_sdk_ec2.types.asn_association_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> AsnAssociation:
    out: AsnAssociation = {}  # type: ignore[typeddict-item]
    child_asn = el.find("Asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.asn_association_state

        out["state"] = aws_sdk_ec2.types.asn_association_state.deserialize_ec2_query(
            child_state
        )
    return out
