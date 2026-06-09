"""Generated from Smithy shape ``com.amazonaws.s3#BucketAlreadyExists``."""

from typing import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class BucketAlreadyExists_(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: BucketAlreadyExists_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> BucketAlreadyExists_:
    out: BucketAlreadyExists_ = {}  # type: ignore[typeddict-item]
    return out


class BucketAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#BucketAlreadyExists``."""

    code: str | None = "BucketAlreadyExists"

    def __init__(self, data: BucketAlreadyExists_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BucketAlreadyExists",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "BucketAlreadyExists":
        return cls(deserialize_xml(el))
