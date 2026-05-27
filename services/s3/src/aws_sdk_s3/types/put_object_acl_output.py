"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectAclOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.request_charged


class PutObjectAclOutput(TypedDict):
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: PutObjectAclOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PutObjectAclOutput:
    out: PutObjectAclOutput = {}  # type: ignore[typeddict-item]
    return out
