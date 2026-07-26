"""Generated from Smithy shape ``com.amazonaws.ec2#AttachVpnGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_attachment


class AttachVpnGatewayResult(TypedDict, closed=True):
    vpc_attachment: NotRequired["capo_ec2.types.vpc_attachment.VpcAttachment"]
    """<p>Information about the attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttachVpnGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc_attachment" in value:
        import capo_ec2.types.vpc_attachment

        capo_ec2.types.vpc_attachment.serialize_ec2_query(
            value["vpc_attachment"], pairs, f"{prefix}.Attachment"
        )


def deserialize_ec2_query(el: Element) -> AttachVpnGatewayResult:
    out: AttachVpnGatewayResult = {}  # type: ignore[typeddict-item]
    child_vpc_attachment = el.find("Attachment")
    if child_vpc_attachment is not None:
        import capo_ec2.types.vpc_attachment

        out["vpc_attachment"] = capo_ec2.types.vpc_attachment.deserialize_ec2_query(
            child_vpc_attachment
        )
    return out
