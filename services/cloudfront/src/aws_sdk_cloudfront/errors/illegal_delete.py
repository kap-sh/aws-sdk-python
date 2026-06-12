"""Generated from Smithy shape ``com.amazonaws.cloudfront#IllegalDelete``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class IllegalDelete_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: IllegalDelete_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> IllegalDelete_:
    out: IllegalDelete_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class IllegalDelete(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#IllegalDelete``."""

    code: str | None = "IllegalDelete"

    def __init__(self, data: IllegalDelete_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalDelete",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "IllegalDelete":
        return cls(deserialize_xml(el))
