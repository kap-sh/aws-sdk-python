"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldPatterns``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.field_pattern_list
    import aws_sdk_cloudfront.types.integer


class FieldPatterns(TypedDict):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of field-level encryption field patterns.</p>"""
    items: NotRequired["aws_sdk_cloudfront.types.field_pattern_list.FieldPatternList"]
    """<p>An array of the field-level encryption field patterns.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FieldPatterns, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.field_pattern_list

        aws_sdk_cloudfront.types.field_pattern_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> FieldPatterns:
    out: FieldPatterns = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("FieldPatterns.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.field_pattern_list

        out["items"] = aws_sdk_cloudfront.types.field_pattern_list.deserialize_xml(
            child_items
        )
    return out
