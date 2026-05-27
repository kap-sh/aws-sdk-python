"""Generated from Smithy shape ``com.amazonaws.s3#EncryptionTypeMismatch``."""

from typing import TypedDict
from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class EncryptionTypeMismatch_(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(value: EncryptionTypeMismatch_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> EncryptionTypeMismatch_:
    out: EncryptionTypeMismatch_ = {}  # type: ignore[typeddict-item]
    return out


class EncryptionTypeMismatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#EncryptionTypeMismatch``."""

    code: str | None = "EncryptionTypeMismatch"

    def __init__(self, data: EncryptionTypeMismatch_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EncryptionTypeMismatch",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "EncryptionTypeMismatch":
        return cls(deserialize_xml(el))
