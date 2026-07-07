"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContentTypeProfiles``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.content_type_profile_list
    import aws_sdk_cloudfront.types.integer


class ContentTypeProfiles(TypedDict, closed=True):
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of field-level encryption content type-profile mappings.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.content_type_profile_list.ContentTypeProfileList"
    ]
    """<p>Items in a field-level encryption content type-profile mapping.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ContentTypeProfiles, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.content_type_profile_list

        aws_sdk_cloudfront.types.content_type_profile_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> ContentTypeProfiles:
    out: ContentTypeProfiles = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("ContentTypeProfiles.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.content_type_profile_list

        out["items"] = (
            aws_sdk_cloudfront.types.content_type_profile_list.deserialize_xml(
                child_items
            )
        )
    return out
