"""Generated from Smithy shape ``com.amazonaws.s3#AnnotationNameTooLong``."""

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import ServiceError


class AnnotationNameTooLong_(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(value: AnnotationNameTooLong_, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> AnnotationNameTooLong_:
    out: AnnotationNameTooLong_ = {}  # type: ignore[typeddict-item]
    return out


class AnnotationNameTooLong(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3#AnnotationNameTooLong``."""

    code: str | None = "AnnotationNameTooLong"

    def __init__(self, data: AnnotationNameTooLong_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AnnotationNameTooLong",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None
    ) -> "AnnotationNameTooLong":
        return cls(deserialize_xml(el), message)
