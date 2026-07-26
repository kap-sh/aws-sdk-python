"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListKeyValueStoresResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.key_value_store_list


class ListKeyValueStoresResult(TypedDict, closed=True):
    key_value_store_list: NotRequired[
        "capo_cloudfront.types.key_value_store_list.KeyValueStoreList"
    ]
    """<p>The resulting key value stores list.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListKeyValueStoresResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key_value_store_list" in value:
        import capo_cloudfront.types.key_value_store_list

        capo_cloudfront.types.key_value_store_list.serialize_xml(
            value["key_value_store_list"], el, "KeyValueStoreList"
        )


def deserialize_xml(el: Element) -> ListKeyValueStoresResult:
    out: ListKeyValueStoresResult = {}  # type: ignore[typeddict-item]
    child_key_value_store_list = el.find("KeyValueStoreList")
    if child_key_value_store_list is not None:
        import capo_cloudfront.types.key_value_store_list

        out["key_value_store_list"] = (
            capo_cloudfront.types.key_value_store_list.deserialize_xml(
                child_key_value_store_list
            )
        )
    return out
