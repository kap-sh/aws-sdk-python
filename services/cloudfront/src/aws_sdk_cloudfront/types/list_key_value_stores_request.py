"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListKeyValueStoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListKeyValueStoresRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The marker associated with the key value stores list.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of items in the key value stores list.</p>"""
    status: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The status of the request for the key value stores list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListKeyValueStoresRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListKeyValueStoresRequest:
    out: ListKeyValueStoresRequest = {}  # type: ignore[typeddict-item]
    return out
