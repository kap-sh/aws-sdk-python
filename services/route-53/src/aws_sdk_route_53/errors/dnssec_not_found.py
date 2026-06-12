"""Generated from Smithy shape ``com.amazonaws.route53#DNSSECNotFound``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.error_message


class DNSSECNotFound_(TypedDict):
    message: NotRequired["aws_sdk_route_53.types.error_message.ErrorMessage"]


# --- restXml ser/de ---
def serialize_xml(value: DNSSECNotFound_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "message").text = str(value["message"])


def deserialize_xml(el: Element) -> DNSSECNotFound_:
    out: DNSSECNotFound_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DNSSECNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#DNSSECNotFound``."""

    code: str | None = "DNSSECNotFound"

    def __init__(self, data: DNSSECNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DNSSECNotFound",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "DNSSECNotFound":
        return cls(deserialize_xml(el))
