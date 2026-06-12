"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionIdOwnerList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.distribution_id_owner_item_list
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class DistributionIdOwnerList(TypedDict):
    marker: "aws_sdk_cloudfront.types.string.string"
    """<p>Use this field when paginating results to indicate where to begin in your list of <code>DistributionIdOwner</code> objects. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    next_marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.</p>"""
    max_items: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The maximum number of <code>DistributionIdOwner</code> objects to return.</p>"""
    is_truncated: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>A flag that indicates whether more <code>DistributionIdOwner</code> objects remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more results in the list.</p>"""
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>Specifies the actual number of <code>DistributionIdOwner</code> objects included in the list for the current page.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.distribution_id_owner_item_list.DistributionIdOwnerItemList"
    ]
    """<p>The number of <code>DistributionIdOwner</code> objects.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionIdOwnerList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Marker").text = str(value["marker"])
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])
    SubElement(el, "IsTruncated").text = "true" if value["is_truncated"] else "false"
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.distribution_id_owner_item_list

        aws_sdk_cloudfront.types.distribution_id_owner_item_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> DistributionIdOwnerList:
    out: DistributionIdOwnerList = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    else:
        raise DeserializationError("DistributionIdOwnerList.marker required")
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        raise DeserializationError("DistributionIdOwnerList.max_items required")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        raise DeserializationError("DistributionIdOwnerList.is_truncated required")
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("DistributionIdOwnerList.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.distribution_id_owner_item_list

        out["items"] = (
            aws_sdk_cloudfront.types.distribution_id_owner_item_list.deserialize_xml(
                child_items
            )
        )
    return out
