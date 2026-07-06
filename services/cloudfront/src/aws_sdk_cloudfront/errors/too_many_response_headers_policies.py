"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyResponseHeadersPolicies``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class TooManyResponseHeadersPolicies_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: TooManyResponseHeadersPolicies_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TooManyResponseHeadersPolicies_:
    out: TooManyResponseHeadersPolicies_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyResponseHeadersPolicies(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyResponseHeadersPolicies``."""

    code: str | None = "TooManyResponseHeadersPolicies"

    def __init__(self, data: TooManyResponseHeadersPolicies_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyResponseHeadersPolicies",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "TooManyResponseHeadersPolicies":
        return cls(deserialize_xml(el))
