"""Generated from Smithy shape ``com.amazonaws.ses#SendRawEmailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.message_id


class SendRawEmailResponse(TypedDict, closed=True):
    message_id: "aws_sdk_ses.types.message_id.MessageId"
    """<p>The unique message identifier returned from the <code>SendRawEmail</code> action. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendRawEmailResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.MessageId", str(value["message_id"])))


def deserialize_query(el: Element) -> SendRawEmailResponse:
    out: SendRawEmailResponse = {}  # type: ignore[typeddict-item]
    child_message_id = el.find("MessageId")
    if child_message_id is not None:
        out["message_id"] = str(child_message_id.text or "")
    else:
        raise DeserializationError("SendRawEmailResponse.message_id required")
    return out
