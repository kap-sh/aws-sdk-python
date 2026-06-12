"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyRealtimeLogConfigs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class TooManyRealtimeLogConfigs_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: TooManyRealtimeLogConfigs_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TooManyRealtimeLogConfigs_:
    out: TooManyRealtimeLogConfigs_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyRealtimeLogConfigs(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyRealtimeLogConfigs``."""

    code: str | None = "TooManyRealtimeLogConfigs"

    def __init__(self, data: TooManyRealtimeLogConfigs_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRealtimeLogConfigs",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "TooManyRealtimeLogConfigs":
        return cls(deserialize_xml(el))
