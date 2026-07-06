"""Generated from Smithy shape ``com.amazonaws.cloudfront#Paths``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.path_list


class Paths(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of invalidation paths specified for the objects that you want to invalidate.</p>"""
    items: NotRequired["aws_sdk_cloudfront.types.path_list.PathList"]
    """<p>A complex type that contains a list of the paths that you want to invalidate.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Paths, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.path_list

        aws_sdk_cloudfront.types.path_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> Paths:
    out: Paths = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("Paths.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.path_list

        out["items"] = aws_sdk_cloudfront.types.path_list.deserialize_xml(child_items)
    return out
