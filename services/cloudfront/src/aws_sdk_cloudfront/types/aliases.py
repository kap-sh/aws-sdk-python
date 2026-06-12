"""Generated from Smithy shape ``com.amazonaws.cloudfront#Aliases``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.alias_list
    import aws_sdk_cloudfront.types.integer


class Aliases(TypedDict):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of CNAME aliases, if any, that you want to associate with this distribution.</p>"""
    items: NotRequired["aws_sdk_cloudfront.types.alias_list.AliasList"]
    """<p>A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Aliases, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.alias_list

        aws_sdk_cloudfront.types.alias_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> Aliases:
    out: Aliases = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("Aliases.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.alias_list

        out["items"] = aws_sdk_cloudfront.types.alias_list.deserialize_xml(child_items)
    return out
