"""Generated from Smithy shape ``com.amazonaws.s3#IdempotencyParameterMismatch``."""

from typing import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import ServiceError


class IdempotencyParameterMismatch_(TypedDict):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: IdempotencyParameterMismatch_, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> IdempotencyParameterMismatch_:
    out: IdempotencyParameterMismatch_ = {}  # type: ignore[typeddict-item]
    return out


class IdempotencyParameterMismatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#IdempotencyParameterMismatch``."""

    code: str | None = "IdempotencyParameterMismatch"

    def __init__(self, data: IdempotencyParameterMismatch_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotencyParameterMismatch",
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element) -> "IdempotencyParameterMismatch":
        return cls(deserialize_xml(el))
