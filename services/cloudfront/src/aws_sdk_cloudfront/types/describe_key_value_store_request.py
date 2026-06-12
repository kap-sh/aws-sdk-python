"""Generated from Smithy shape ``com.amazonaws.cloudfront#DescribeKeyValueStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_value_store_name


class DescribeKeyValueStoreRequest(TypedDict):
    name: "aws_sdk_cloudfront.types.key_value_store_name.KeyValueStoreName"
    """<p>The name of the key value store.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DescribeKeyValueStoreRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DescribeKeyValueStoreRequest:
    out: DescribeKeyValueStoreRequest = {}  # type: ignore[typeddict-item]
    return out
