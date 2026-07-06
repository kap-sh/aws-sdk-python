"""Generated from Smithy shape ``com.amazonaws.sts#DecodeAuthorizationMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sts._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sts.types.decoded_message_type


class DecodeAuthorizationMessageResponse(TypedDict, closed=True):
    decoded_message: NotRequired[
        "aws_sdk_sts.types.decoded_message_type.decodedMessageType"
    ]
    """<p>The API returns a response with the decoded message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DecodeAuthorizationMessageResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "decoded_message" in value:
        pairs.append((f"{prefix}.DecodedMessage", str(value["decoded_message"])))


def deserialize_query(el: Element) -> DecodeAuthorizationMessageResponse:
    out: DecodeAuthorizationMessageResponse = {}  # type: ignore[typeddict-item]
    child_decoded_message = el.find("DecodedMessage")
    if child_decoded_message is not None:
        out["decoded_message"] = str(child_decoded_message.text or "")
    return out
