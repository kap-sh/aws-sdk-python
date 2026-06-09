"""Generated from Smithy shape ``com.amazonaws.s3#NotFound``."""

from typing import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class NotFound_(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: NotFound_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> NotFound_:
    out: NotFound_ = {}  # type: ignore[typeddict-item]
    return out


class NotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#NotFound``."""

    code: str | None = "NotFound"

    def __init__(self, data: NotFound_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="NotFound"
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "NotFound":
        return cls(deserialize_xml(el))
