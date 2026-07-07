"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyStreamingDistributionCNAMEs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class TooManyStreamingDistributionCNAMEs_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: TooManyStreamingDistributionCNAMEs_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TooManyStreamingDistributionCNAMEs_:
    out: TooManyStreamingDistributionCNAMEs_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyStreamingDistributionCNAMEs(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyStreamingDistributionCNAMEs``."""

    code: str | None = "TooManyStreamingDistributionCNAMEs"

    def __init__(self, data: TooManyStreamingDistributionCNAMEs_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyStreamingDistributionCNAMEs",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "TooManyStreamingDistributionCNAMEs":
        return cls(deserialize_xml(el))
