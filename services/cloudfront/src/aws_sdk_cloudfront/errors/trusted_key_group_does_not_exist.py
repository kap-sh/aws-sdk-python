"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustedKeyGroupDoesNotExist``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class TrustedKeyGroupDoesNotExist_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: TrustedKeyGroupDoesNotExist_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> TrustedKeyGroupDoesNotExist_:
    out: TrustedKeyGroupDoesNotExist_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TrustedKeyGroupDoesNotExist(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#TrustedKeyGroupDoesNotExist``."""

    code: str | None = "TrustedKeyGroupDoesNotExist"

    def __init__(self, data: TrustedKeyGroupDoesNotExist_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TrustedKeyGroupDoesNotExist",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "TrustedKeyGroupDoesNotExist":
        return cls(deserialize_xml(el))
