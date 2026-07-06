"""Generated from Smithy shape ``com.amazonaws.s3#InvalidRequest``."""

from typing_extensions import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class InvalidRequest_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: InvalidRequest_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> InvalidRequest_:
    out: InvalidRequest_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidRequest(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#InvalidRequest``."""

    code: str | None = "InvalidRequest"

    def __init__(self, data: InvalidRequest_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequest",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidRequest":
        return cls(deserialize_xml(el))
