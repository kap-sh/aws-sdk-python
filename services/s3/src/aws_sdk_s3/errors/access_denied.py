"""Generated from Smithy shape ``com.amazonaws.s3#AccessDenied``."""

from typing import TypedDict
from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class AccessDenied_(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: AccessDenied_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> AccessDenied_:
    out: AccessDenied_ = {}  # type: ignore[typeddict-item]
    return out


class AccessDenied(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#AccessDenied``."""

    code: str | None = "AccessDenied"

    def __init__(self, data: AccessDenied_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="AccessDenied"
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "AccessDenied":
        return cls(deserialize_xml(el))
