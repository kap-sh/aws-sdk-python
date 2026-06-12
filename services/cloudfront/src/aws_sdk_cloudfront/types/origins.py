"""Generated from Smithy shape ``com.amazonaws.cloudfront#Origins``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.origin_list


class Origins(TypedDict):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of origins for this distribution.</p>"""
    items: "aws_sdk_cloudfront.types.origin_list.OriginList"
    """<p>A list of origins.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Origins, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import aws_sdk_cloudfront.types.origin_list

    aws_sdk_cloudfront.types.origin_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> Origins:
    out: Origins = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("Origins.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.origin_list

        out["items"] = aws_sdk_cloudfront.types.origin_list.deserialize_xml(child_items)
    else:
        raise DeserializationError("Origins.items required")
    return out
