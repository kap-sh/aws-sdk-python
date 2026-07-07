"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateKeyValueStoreResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_value_store
    import aws_sdk_cloudfront.types.string


class CreateKeyValueStoreResult(TypedDict, closed=True):
    key_value_store: NotRequired[
        "aws_sdk_cloudfront.types.key_value_store.KeyValueStore"
    ]
    """<p>The resulting key value store.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The <code>ETag</code> in the resulting key value store.</p>"""
    location: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The location of the resulting key value store.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateKeyValueStoreResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key_value_store" in value:
        import aws_sdk_cloudfront.types.key_value_store

        aws_sdk_cloudfront.types.key_value_store.serialize_xml(
            value["key_value_store"], el, "KeyValueStore"
        )


def deserialize_xml(el: Element) -> CreateKeyValueStoreResult:
    out: CreateKeyValueStoreResult = {}  # type: ignore[typeddict-item]
    child_key_value_store = el.find("KeyValueStore")
    if child_key_value_store is not None:
        import aws_sdk_cloudfront.types.key_value_store

        out["key_value_store"] = (
            aws_sdk_cloudfront.types.key_value_store.deserialize_xml(
                child_key_value_store
            )
        )
    return out
