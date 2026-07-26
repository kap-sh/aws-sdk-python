"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetFieldLevelEncryptionProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class GetFieldLevelEncryptionProfileRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>Get the ID for the field-level encryption profile information.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetFieldLevelEncryptionProfileRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetFieldLevelEncryptionProfileRequest:
    out: GetFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
    return out
