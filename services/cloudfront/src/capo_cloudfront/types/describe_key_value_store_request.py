"""Generated from Smithy shape ``com.amazonaws.cloudfront#DescribeKeyValueStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.key_value_store_name


class DescribeKeyValueStoreRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.key_value_store_name.KeyValueStoreName"
    """<p>The name of the key value store.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DescribeKeyValueStoreRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DescribeKeyValueStoreRequest:
    out: DescribeKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
    return out
