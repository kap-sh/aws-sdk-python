"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGatewayAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attachment_status
    import capo_ec2.types.string


class InternetGatewayAttachment(TypedDict, closed=True):
    state: NotRequired["capo_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The current state of the attachment. For an internet gateway, the state is <code>available</code> when attached to a VPC; otherwise, this value is not returned.</p>"""
    vpc_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InternetGatewayAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        import capo_ec2.types.attachment_status

        capo_ec2.types.attachment_status.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> InternetGatewayAttachment:
    out: InternetGatewayAttachment = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.attachment_status

        out["state"] = capo_ec2.types.attachment_status.deserialize_ec2_query(
            child_state
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
