"""Generated from Smithy shape ``com.amazonaws.s3#InvalidWriteOffset``."""

from typing import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class InvalidWriteOffset_(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: InvalidWriteOffset_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> InvalidWriteOffset_:
    out: InvalidWriteOffset_ = {}  # type: ignore[typeddict-item]
    return out


class InvalidWriteOffset(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#InvalidWriteOffset``."""

    code: str | None = "InvalidWriteOffset"

    def __init__(self, data: InvalidWriteOffset_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidWriteOffset",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "InvalidWriteOffset":
        return cls(deserialize_xml(el))
