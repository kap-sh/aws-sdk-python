"""Generated from Smithy shape ``com.amazonaws.cloudfront#NoSuchInvalidation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class NoSuchInvalidation_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: NoSuchInvalidation_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> NoSuchInvalidation_:
    out: NoSuchInvalidation_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class NoSuchInvalidation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#NoSuchInvalidation``."""

    code: str | None = "NoSuchInvalidation"

    def __init__(self, data: NoSuchInvalidation_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchInvalidation",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "NoSuchInvalidation":
        return cls(deserialize_xml(el))
