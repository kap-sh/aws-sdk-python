"""Generated from Smithy shape ``com.amazonaws.route53#InvalidChangeBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.error_message
    import aws_sdk_route_53.types.error_messages


class InvalidChangeBatch_(TypedDict, closed=True):
    messages: NotRequired["aws_sdk_route_53.types.error_messages.ErrorMessages"]
    """<p></p>"""
    message: NotRequired["aws_sdk_route_53.types.error_message.ErrorMessage"]


# --- restXml ser/de ---
def serialize_xml(value: InvalidChangeBatch_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "messages" in value:
        import aws_sdk_route_53.types.error_messages

        aws_sdk_route_53.types.error_messages.serialize_xml(
            value["messages"], el, "messages"
        )
    if "message" in value:
        SubElement(el, "message").text = str(value["message"])


def deserialize_xml(el: Element) -> InvalidChangeBatch_:
    out: InvalidChangeBatch_ = {}  # type: ignore[typeddict-item]
    child_messages = el.find("messages")
    if child_messages is not None:
        import aws_sdk_route_53.types.error_messages

        out["messages"] = aws_sdk_route_53.types.error_messages.deserialize_xml(
            child_messages
        )
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidChangeBatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#InvalidChangeBatch``."""

    code: str | None = "InvalidChangeBatch"

    def __init__(self, data: InvalidChangeBatch_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidChangeBatch",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidChangeBatch":
        return cls(deserialize_xml(el))
