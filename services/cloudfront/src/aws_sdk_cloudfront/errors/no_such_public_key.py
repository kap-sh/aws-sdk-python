"""Generated from Smithy shape ``com.amazonaws.cloudfront#NoSuchPublicKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class NoSuchPublicKey_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: NoSuchPublicKey_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> NoSuchPublicKey_:
    out: NoSuchPublicKey_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class NoSuchPublicKey(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#NoSuchPublicKey``."""

    code: str | None = "NoSuchPublicKey"

    def __init__(self, data: NoSuchPublicKey_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchPublicKey",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "NoSuchPublicKey":
        return cls(deserialize_xml(el))
