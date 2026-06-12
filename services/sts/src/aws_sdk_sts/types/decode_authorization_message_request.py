"""Generated from Smithy shape ``com.amazonaws.sts#DecodeAuthorizationMessageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sts.types.encoded_message_type


class DecodeAuthorizationMessageRequest(TypedDict):
    encoded_message: "aws_sdk_sts.types.encoded_message_type.encodedMessageType"
    """<p>The encoded message that was returned with the response.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DecodeAuthorizationMessageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.EncodedMessage", str(value["encoded_message"])))


def deserialize_query(el: Element) -> DecodeAuthorizationMessageRequest:
    out: DecodeAuthorizationMessageRequest = {}  # type: ignore[typeddict-item]
    child_encoded_message = el.find("EncodedMessage")
    if child_encoded_message is not None:
        out["encoded_message"] = str(child_encoded_message.text or "")
    else:
        raise DeserializationError(
            "DecodeAuthorizationMessageRequest.encoded_message required"
        )
    return out
