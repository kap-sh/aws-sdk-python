"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneNotEmpty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.error_message


class HostedZoneNotEmpty_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_route_53.types.error_message.ErrorMessage"]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneNotEmpty_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "message").text = str(value["message"])


def deserialize_xml(el: Element) -> HostedZoneNotEmpty_:
    out: HostedZoneNotEmpty_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class HostedZoneNotEmpty(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#HostedZoneNotEmpty``."""

    code: str | None = "HostedZoneNotEmpty"

    def __init__(self, data: HostedZoneNotEmpty_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="HostedZoneNotEmpty",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "HostedZoneNotEmpty":
        return cls(deserialize_xml(el))
