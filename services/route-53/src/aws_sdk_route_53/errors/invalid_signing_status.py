"""Generated from Smithy shape ``com.amazonaws.route53#InvalidSigningStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.error_message


class InvalidSigningStatus_(TypedDict):
    message: NotRequired["aws_sdk_route_53.types.error_message.ErrorMessage"]


# --- restXml ser/de ---
def serialize_xml(value: InvalidSigningStatus_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "message").text = str(value["message"])


def deserialize_xml(el: Element) -> InvalidSigningStatus_:
    out: InvalidSigningStatus_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidSigningStatus(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#InvalidSigningStatus``."""

    code: str | None = "InvalidSigningStatus"

    def __init__(self, data: InvalidSigningStatus_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSigningStatus",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidSigningStatus":
        return cls(deserialize_xml(el))
