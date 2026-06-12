"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContinuousDeploymentPolicyInUse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class ContinuousDeploymentPolicyInUse_(TypedDict):
    message: NotRequired["aws_sdk_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: ContinuousDeploymentPolicyInUse_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])


def deserialize_xml(el: Element) -> ContinuousDeploymentPolicyInUse_:
    out: ContinuousDeploymentPolicyInUse_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ContinuousDeploymentPolicyInUse(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudfront#ContinuousDeploymentPolicyInUse``."""

    code: str | None = "ContinuousDeploymentPolicyInUse"

    def __init__(self, data: ContinuousDeploymentPolicyInUse_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContinuousDeploymentPolicyInUse",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "ContinuousDeploymentPolicyInUse":
        return cls(deserialize_xml(el))
