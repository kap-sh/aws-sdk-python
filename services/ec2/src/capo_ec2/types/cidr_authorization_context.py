"""Generated from Smithy shape ``com.amazonaws.ec2#CidrAuthorizationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class CidrAuthorizationContext(TypedDict, closed=True):
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>The plain-text authorization message for the prefix and account.</p>"""
    signature: NotRequired["capo_ec2.types.string.String"]
    """<p>The signed authorization message for the prefix and account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CidrAuthorizationContext, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    if "signature" in value:
        pairs.append((f"{prefix}.Signature", str(value["signature"])))


def deserialize_ec2_query(el: Element) -> CidrAuthorizationContext:
    out: CidrAuthorizationContext = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_signature = el.find("Signature")
    if child_signature is not None:
        out["signature"] = str(child_signature.text or "")
    return out
