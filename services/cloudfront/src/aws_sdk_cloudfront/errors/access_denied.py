"""Generated from Smithy shape ``com.amazonaws.cloudfront#AccessDenied``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class AccessDenied_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: AccessDenied_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> AccessDenied_:
    out: AccessDenied_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class AccessDenied(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#AccessDenied``."""

    code: str | None = "AccessDenied"

    def __init__(self, data: AccessDenied_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="AccessDenied"
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "AccessDenied":
        return cls(deserialize_xml(el))
