"""Generated from Smithy shape ``com.amazonaws.s3#BucketAlreadyOwnedByYou``."""

from typing import TypedDict
from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class BucketAlreadyOwnedByYou_(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: BucketAlreadyOwnedByYou_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> BucketAlreadyOwnedByYou_:
    out: BucketAlreadyOwnedByYou_ = {}  # type: ignore[typeddict-item]
    return out


class BucketAlreadyOwnedByYou(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#BucketAlreadyOwnedByYou``."""

    code: str | None = "BucketAlreadyOwnedByYou"

    def __init__(self, data: BucketAlreadyOwnedByYou_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BucketAlreadyOwnedByYou",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "BucketAlreadyOwnedByYou":
        return cls(deserialize_xml(el))
