"""Generated from Smithy shape ``com.amazonaws.ses#SendBounceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.message_id


class SendBounceResponse(TypedDict, closed=True):
    message_id: NotRequired["aws_sdk_ses.types.message_id.MessageId"]
    """<p>The message ID of the bounce message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendBounceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message_id" in value:
        pairs.append((f"{prefix}.MessageId", str(value["message_id"])))


def deserialize_query(el: Element) -> SendBounceResponse:
    out: SendBounceResponse = {}  # type: ignore[typeddict-item]
    child_message_id = el.find("MessageId")
    if child_message_id is not None:
        out["message_id"] = str(child_message_id.text or "")
    return out
