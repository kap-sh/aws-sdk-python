"""Generated from Smithy shape ``com.amazonaws.s3#NoSuchBucket``."""

from typing import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class NoSuchBucket_(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: NoSuchBucket_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> NoSuchBucket_:
    out: NoSuchBucket_ = {}  # type: ignore[typeddict-item]
    return out


class NoSuchBucket(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#NoSuchBucket``."""

    code: str | None = "NoSuchBucket"

    def __init__(self, data: NoSuchBucket_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="NoSuchBucket"
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "NoSuchBucket":
        return cls(deserialize_xml(el))
