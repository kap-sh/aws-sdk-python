"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFieldLevelEncryptionProfileConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class GetFieldLevelEncryptionProfileConfigRequest(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>Get the ID for the field-level encryption profile configuration information.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetFieldLevelEncryptionProfileConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetFieldLevelEncryptionProfileConfigRequest:
    out: GetFieldLevelEncryptionProfileConfigRequest = {}  # type: ignore[typeddict-item]
    return out
