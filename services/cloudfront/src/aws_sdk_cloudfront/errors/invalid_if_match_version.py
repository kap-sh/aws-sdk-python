"""Generated from Smithy shape ``com.amazonaws.cloudfront#InvalidIfMatchVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class InvalidIfMatchVersion_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: InvalidIfMatchVersion_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> InvalidIfMatchVersion_:
    out: InvalidIfMatchVersion_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidIfMatchVersion(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#InvalidIfMatchVersion``."""

    code: str | None = "InvalidIfMatchVersion"

    def __init__(self, data: InvalidIfMatchVersion_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidIfMatchVersion",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidIfMatchVersion":
        return cls(deserialize_xml(el))
