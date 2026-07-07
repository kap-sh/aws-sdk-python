"""Generated from Smithy shape ``com.amazonaws.ses#SendTemplatedEmailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.message_id


class SendTemplatedEmailResponse(TypedDict, closed=True):
    message_id: "aws_sdk_ses.types.message_id.MessageId"
    """<p>The unique message identifier returned from the <code>SendTemplatedEmail</code> action. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendTemplatedEmailResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.MessageId", str(value["message_id"])))


def deserialize_query(el: Element) -> SendTemplatedEmailResponse:
    out: SendTemplatedEmailResponse = {}  # type: ignore[typeddict-item]
    child_message_id = el.find("MessageId")
    if child_message_id is not None:
        out["message_id"] = str(child_message_id.text or "")
    else:
        raise DeserializationError("SendTemplatedEmailResponse.message_id required")
    return out
