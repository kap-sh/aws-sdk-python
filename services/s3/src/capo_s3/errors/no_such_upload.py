"""Generated from Smithy shape ``com.amazonaws.s3#NoSuchUpload``."""

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class NoSuchUpload_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: NoSuchUpload_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> NoSuchUpload_:
    out: NoSuchUpload_ = {}  # type: ignore[typeddict-item]
    return out


class NoSuchUpload(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#NoSuchUpload``."""

    code: str | None = "NoSuchUpload"

    def __init__(self, data: NoSuchUpload_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchUpload",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_xml(cls, el: Element, message: str | None = None) -> "NoSuchUpload":
        return cls(deserialize_xml(el), message)
