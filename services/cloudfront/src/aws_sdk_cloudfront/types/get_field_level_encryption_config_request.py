"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFieldLevelEncryptionConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetFieldLevelEncryptionConfigRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>Request the ID for the field-level encryption configuration information.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetFieldLevelEncryptionConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetFieldLevelEncryptionConfigRequest:
    out: GetFieldLevelEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
    return out
