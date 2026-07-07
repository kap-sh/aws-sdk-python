"""Generated from Smithy shape ``com.amazonaws.cloudfront#RealtimeLogConfigInUse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class RealtimeLogConfigInUse_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: RealtimeLogConfigInUse_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> RealtimeLogConfigInUse_:
    out: RealtimeLogConfigInUse_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class RealtimeLogConfigInUse(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#RealtimeLogConfigInUse``."""

    code: str | None = "RealtimeLogConfigInUse"

    def __init__(self, data: RealtimeLogConfigInUse_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RealtimeLogConfigInUse",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "RealtimeLogConfigInUse":
        return cls(deserialize_xml(el))
