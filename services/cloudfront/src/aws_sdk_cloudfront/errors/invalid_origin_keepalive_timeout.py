"""Generated from Smithy shape ``com.amazonaws.cloudfront#InvalidOriginKeepaliveTimeout``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class InvalidOriginKeepaliveTimeout_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: InvalidOriginKeepaliveTimeout_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> InvalidOriginKeepaliveTimeout_:
    out: InvalidOriginKeepaliveTimeout_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidOriginKeepaliveTimeout(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#InvalidOriginKeepaliveTimeout``."""

    code: str | None = "InvalidOriginKeepaliveTimeout"

    def __init__(self, data: InvalidOriginKeepaliveTimeout_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidOriginKeepaliveTimeout",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidOriginKeepaliveTimeout":
        return cls(deserialize_xml(el))
