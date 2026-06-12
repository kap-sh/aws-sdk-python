"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyCookieNamesInWhiteList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class TooManyCookieNamesInWhiteList_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: TooManyCookieNamesInWhiteList_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TooManyCookieNamesInWhiteList_:
    out: TooManyCookieNamesInWhiteList_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyCookieNamesInWhiteList(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyCookieNamesInWhiteList``."""

    code: str | None = "TooManyCookieNamesInWhiteList"

    def __init__(self, data: TooManyCookieNamesInWhiteList_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyCookieNamesInWhiteList",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "TooManyCookieNamesInWhiteList":
        return cls(deserialize_xml(el))
