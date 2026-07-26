"""Generated from Smithy shape ``com.amazonaws.s3control#InvalidNextTokenException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import ServiceError

if TYPE_CHECKING:
    import capo_s3_control.types.exception_message


class InvalidNextTokenException_(TypedDict, closed=True):
    message: NotRequired["capo_s3_control.types.exception_message.ExceptionMessage"]


# --- restXml ser/de ---
def serialize_xml(value: InvalidNextTokenException_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> InvalidNextTokenException_:
    out: InvalidNextTokenException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidNextTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3control#InvalidNextTokenException``."""

    code: str | None = "InvalidNextTokenException"

    def __init__(self, data: InvalidNextTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNextTokenException",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidNextTokenException":
        return cls(deserialize_xml(el))
