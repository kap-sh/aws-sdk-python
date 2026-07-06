"""Generated from Smithy shape ``com.amazonaws.cloudfront#TooManyDistributionsAssociatedToOriginAccessControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class TooManyDistributionsAssociatedToOriginAccessControl_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: TooManyDistributionsAssociatedToOriginAccessControl_,
    parent: Element,
    tag: str,
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(
    el: Element,
) -> TooManyDistributionsAssociatedToOriginAccessControl_:
    out: TooManyDistributionsAssociatedToOriginAccessControl_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyDistributionsAssociatedToOriginAccessControl(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TooManyDistributionsAssociatedToOriginAccessControl``."""

    code: str | None = "TooManyDistributionsAssociatedToOriginAccessControl"

    def __init__(self, data: TooManyDistributionsAssociatedToOriginAccessControl_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyDistributionsAssociatedToOriginAccessControl",
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element
    ) -> "TooManyDistributionsAssociatedToOriginAccessControl":
        return cls(deserialize_xml(el))
