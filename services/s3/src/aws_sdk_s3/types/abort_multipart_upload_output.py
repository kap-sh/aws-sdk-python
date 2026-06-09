"""Generated from Smithy shape ``com.amazonaws.s3#AbortMultipartUploadOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.request_charged


class AbortMultipartUploadOutput(TypedDict):
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: AbortMultipartUploadOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> AbortMultipartUploadOutput:
    out: AbortMultipartUploadOutput = {}  # type: ignore[typeddict-item]
    return out
