"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyOriginRequestPolicies``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class TooManyOriginRequestPolicies_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: TooManyOriginRequestPolicies_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TooManyOriginRequestPolicies_:
    out: TooManyOriginRequestPolicies_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyOriginRequestPolicies(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyOriginRequestPolicies``."""

    code: str | None = "TooManyOriginRequestPolicies"

    def __init__(self, data: TooManyOriginRequestPolicies_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyOriginRequestPolicies",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "TooManyOriginRequestPolicies":
        return cls(deserialize_xml(el))
