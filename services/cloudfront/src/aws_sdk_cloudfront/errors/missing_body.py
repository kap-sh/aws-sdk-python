"""Generated from Smithy shape ``com.amazonaws.cloudfront#MissingBody``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class MissingBody_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: MissingBody_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> MissingBody_:
    out: MissingBody_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class MissingBody(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#MissingBody``."""

    code: str | None = "MissingBody"

    def __init__(self, data: MissingBody_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="MissingBody"
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "MissingBody":
        return cls(deserialize_xml(el))
