"""Generated from Smithy shape ``com.amazonaws.cloudfront#NoSuchDistribution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class NoSuchDistribution_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: NoSuchDistribution_, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> NoSuchDistribution_:
    out: NoSuchDistribution_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class NoSuchDistribution(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#NoSuchDistribution``."""

    code: str | None = "NoSuchDistribution"

    def __init__(self, data: NoSuchDistribution_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchDistribution",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "NoSuchDistribution":
        return cls(deserialize_xml(el))
