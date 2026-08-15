"""Generated from Smithy shape ``com.amazonaws.s3#UnsupportedMediaType``."""

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class UnsupportedMediaType_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: UnsupportedMediaType_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> UnsupportedMediaType_:
    out: UnsupportedMediaType_ = {}  # type: ignore[typeddict-item]
    return out


class UnsupportedMediaType(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#UnsupportedMediaType``."""

    code: str | None = "UnsupportedMediaType"

    def __init__(self, data: UnsupportedMediaType_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedMediaType",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None
    ) -> "UnsupportedMediaType":
        return cls(deserialize_xml(el), message)
