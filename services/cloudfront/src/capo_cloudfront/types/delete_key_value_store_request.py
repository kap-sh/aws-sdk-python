"""Generated from Smithy shape ``com.amazonaws.cloudfront#DeleteKeyValueStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.key_value_store_name
    import capo_cloudfront.types.string


class DeleteKeyValueStoreRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.key_value_store_name.KeyValueStoreName"
    """<p>The name of the key value store.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The key value store to delete, if a match occurs.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteKeyValueStoreRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteKeyValueStoreRequest:
    out: DeleteKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
    return out
