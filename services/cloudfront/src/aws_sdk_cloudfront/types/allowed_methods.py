"""Generated from Smithy shape ``com.amazonaws.cloudfront#AllowedMethods``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.cached_methods
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.methods_list


class AllowedMethods(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for <code>GET</code> and <code>HEAD</code> requests), 3 (for <code>GET</code>, <code>HEAD</code>, and <code>OPTIONS</code> requests) and 7 (for <code>GET, HEAD, OPTIONS, PUT, PATCH, POST</code>, and <code>DELETE</code> requests).</p>"""
    items: "aws_sdk_cloudfront.types.methods_list.MethodsList"
    """<p>A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.</p>"""
    cached_methods: NotRequired["aws_sdk_cloudfront.types.cached_methods.CachedMethods"]


# --- restXml ser/de ---
def serialize_xml(value: AllowedMethods, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import aws_sdk_cloudfront.types.methods_list

    aws_sdk_cloudfront.types.methods_list.serialize_xml(value["items"], el, "Items")
    if "cached_methods" in value:
        import aws_sdk_cloudfront.types.cached_methods

        aws_sdk_cloudfront.types.cached_methods.serialize_xml(
            value["cached_methods"], el, "CachedMethods"
        )


def deserialize_xml(el: Element) -> AllowedMethods:
    out: AllowedMethods = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("AllowedMethods.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.methods_list

        out["items"] = aws_sdk_cloudfront.types.methods_list.deserialize_xml(
            child_items
        )
    else:
        raise DeserializationError("AllowedMethods.items required")
    child_cached_methods = el.find("CachedMethods")
    if child_cached_methods is not None:
        import aws_sdk_cloudfront.types.cached_methods

        out["cached_methods"] = aws_sdk_cloudfront.types.cached_methods.deserialize_xml(
            child_cached_methods
        )
    return out
