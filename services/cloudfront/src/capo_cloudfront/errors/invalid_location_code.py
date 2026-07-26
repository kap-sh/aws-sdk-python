"""Generated from Smithy shape ``com.amazonaws.cloudfront#InvalidLocationCode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class InvalidLocationCode_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: InvalidLocationCode_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> InvalidLocationCode_:
    out: InvalidLocationCode_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidLocationCode(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#InvalidLocationCode``."""

    code: str | None = "InvalidLocationCode"

    def __init__(self, data: InvalidLocationCode_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidLocationCode",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidLocationCode":
        return cls(deserialize_xml(el))
