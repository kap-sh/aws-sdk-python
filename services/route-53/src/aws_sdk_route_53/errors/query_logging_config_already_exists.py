"""Generated from Smithy shape ``com.amazonaws.route53#QueryLoggingConfigAlreadyExists``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.error_message


class QueryLoggingConfigAlreadyExists_(TypedDict):
    message: NotRequired["aws_sdk_route_53.types.error_message.ErrorMessage"]


# --- restXml ser/de ---
def serialize_xml(
    value: QueryLoggingConfigAlreadyExists_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "message").text = str(value["message"])


def deserialize_xml(el: Element) -> QueryLoggingConfigAlreadyExists_:
    out: QueryLoggingConfigAlreadyExists_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class QueryLoggingConfigAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#QueryLoggingConfigAlreadyExists``."""

    code: str | None = "QueryLoggingConfigAlreadyExists"

    def __init__(self, data: QueryLoggingConfigAlreadyExists_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="QueryLoggingConfigAlreadyExists",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "QueryLoggingConfigAlreadyExists":
        return cls(deserialize_xml(el))
