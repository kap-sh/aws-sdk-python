"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteFieldLevelEncryptionProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string


class DeleteFieldLevelEncryptionProfileRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>Request the ID of the profile you want to delete from CloudFront.</p>"""
    if_match: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the profile to delete. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteFieldLevelEncryptionProfileRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteFieldLevelEncryptionProfileRequest:
    out: DeleteFieldLevelEncryptionProfileRequest = {}  # type: ignore[typeddict-item]
    return out
