"""Generated from Smithy shape ``com.amazonaws.cloudfront#NoSuchResponseHeadersPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class NoSuchResponseHeadersPolicy_(TypedDict, closed=True):
    message: NotRequired["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: NoSuchResponseHeadersPolicy_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> NoSuchResponseHeadersPolicy_:
    out: NoSuchResponseHeadersPolicy_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class NoSuchResponseHeadersPolicy(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#NoSuchResponseHeadersPolicy``."""

    code: str | None = "NoSuchResponseHeadersPolicy"

    def __init__(self, data: NoSuchResponseHeadersPolicy_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchResponseHeadersPolicy",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None
    ) -> "NoSuchResponseHeadersPolicy":
        return cls(deserialize_xml(el), message)
