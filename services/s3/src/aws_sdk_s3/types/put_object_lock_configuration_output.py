"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectLockConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.request_charged


class PutObjectLockConfigurationOutput(TypedDict, closed=True):
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(
    value: PutObjectLockConfigurationOutput, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PutObjectLockConfigurationOutput:
    out: PutObjectLockConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out
