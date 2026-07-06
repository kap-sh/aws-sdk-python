"""Generated from Smithy shape ``com.amazonaws.ec2#AsnAuthorizationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AsnAuthorizationContext(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The authorization context's message.</p>"""
    signature: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The authorization context's signature.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AsnAuthorizationContext, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    if "signature" in value:
        pairs.append((f"{prefix}.Signature", str(value["signature"])))


def deserialize_ec2_query(el: Element) -> AsnAuthorizationContext:
    out: AsnAuthorizationContext = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_signature = el.find("Signature")
    if child_signature is not None:
        out["signature"] = str(child_signature.text or "")
    return out
