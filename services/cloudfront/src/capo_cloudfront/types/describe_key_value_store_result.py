"""Generated from Smithy shape ``com.amazonaws.cloudfront#DescribeKeyValueStoreResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.key_value_store
    import capo_cloudfront.types.string


class DescribeKeyValueStoreResult(TypedDict, closed=True):
    key_value_store: NotRequired["capo_cloudfront.types.key_value_store.KeyValueStore"]
    """<p>The resulting key value store.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The <code>ETag</code> of the resulting key value store.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DescribeKeyValueStoreResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "key_value_store" in value:
        import capo_cloudfront.types.key_value_store

        capo_cloudfront.types.key_value_store.serialize_xml(
            value["key_value_store"], el, "KeyValueStore"
        )


def deserialize_xml(el: Element) -> DescribeKeyValueStoreResult:
    out: DescribeKeyValueStoreResult = {}  # type: ignore[typeddict-item]
    child_key_value_store = el.find("KeyValueStore")
    if child_key_value_store is not None:
        import capo_cloudfront.types.key_value_store

        out["key_value_store"] = capo_cloudfront.types.key_value_store.deserialize_xml(
            child_key_value_store
        )
    return out
