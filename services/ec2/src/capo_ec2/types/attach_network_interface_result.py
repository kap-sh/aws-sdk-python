"""Generated from Smithy shape ``com.amazonaws.ec2#AttachNetworkInterfaceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class AttachNetworkInterfaceResult(TypedDict, closed=True):
    attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface attachment.</p>"""
    network_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttachNetworkInterfaceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attachment_id" in value:
        pairs.append((f"{key_prefix}AttachmentId", str(value["attachment_id"])))
    if "network_card_index" in value:
        pairs.append(
            (f"{key_prefix}NetworkCardIndex", str(value["network_card_index"]))
        )


def deserialize_ec2_query(el: Element) -> AttachNetworkInterfaceResult:
    out: AttachNetworkInterfaceResult = {}  # type: ignore[typeddict-item]
    child_attachment_id = el.find("attachmentId")
    if child_attachment_id is not None:
        out["attachment_id"] = str(child_attachment_id.text or "")
    child_network_card_index = el.find("networkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    return out
