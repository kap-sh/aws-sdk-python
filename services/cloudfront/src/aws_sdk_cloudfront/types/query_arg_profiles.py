"""Generated from Smithy shape ``com.amazonaws.cloudfront#QueryArgProfiles``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.query_arg_profile_list


class QueryArgProfiles(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>Number of profiles for query argument-profile mapping for field-level encryption.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.query_arg_profile_list.QueryArgProfileList"
    ]
    """<p>Number of items for query argument-profile mapping for field-level encryption.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: QueryArgProfiles, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.query_arg_profile_list

        aws_sdk_cloudfront.types.query_arg_profile_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> QueryArgProfiles:
    out: QueryArgProfiles = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("QueryArgProfiles.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.query_arg_profile_list

        out["items"] = aws_sdk_cloudfront.types.query_arg_profile_list.deserialize_xml(
            child_items
        )
    return out
