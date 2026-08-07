"""Generated from Smithy shape ``com.amazonaws.ses#SendCustomVerificationEmailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.message_id


class SendCustomVerificationEmailResponse(TypedDict, closed=True):
    message_id: NotRequired["capo_ses.types.message_id.MessageId"]
    """<p>The unique message identifier returned from the <code>SendCustomVerificationEmail</code> operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendCustomVerificationEmailResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message_id" in value:
        pairs.append((f"{key_prefix}MessageId", str(value["message_id"])))


def deserialize_query(el: Element) -> SendCustomVerificationEmailResponse:
    out: SendCustomVerificationEmailResponse = {}  # type: ignore[typeddict-item]
    child_message_id = el.find("MessageId")
    if child_message_id is not None:
        out["message_id"] = str(child_message_id.text or "")
    return out
