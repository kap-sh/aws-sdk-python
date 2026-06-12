"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFieldLevelEncryptionProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetFieldLevelEncryptionProfileRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>Get the ID for the field-level encryption profile information.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetFieldLevelEncryptionProfileRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetFieldLevelEncryptionProfileRequest:
    out: GetFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
    return out
