"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListFieldLevelEncryptionProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListFieldLevelEncryptionProfilesRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last profile on that page).</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of field-level encryption profiles you want in the response body. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListFieldLevelEncryptionProfilesRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListFieldLevelEncryptionProfilesRequest:
    out: ListFieldLevelEncryptionProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
