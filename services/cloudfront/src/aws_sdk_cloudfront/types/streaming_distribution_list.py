"""Generated from Smithy shape ``com.amazonaws.cloudfront#StreamingDistributionList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.streaming_distribution_summary_list
    import aws_sdk_cloudfront.types.string


class StreamingDistributionList(TypedDict, closed=True):
    marker: "aws_sdk_cloudfront.types.string.string"
    """<p>The value you provided for the <code>Marker</code> request parameter.</p>"""
    next_marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>If <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value you can use for the <code>Marker</code> request parameter to continue listing your RTMP distributions where they left off.</p>"""
    max_items: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The value you provided for the <code>MaxItems</code> request parameter.</p>"""
    is_truncated: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>A flag that indicates whether more streaming distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more distributions in the list. </p>"""
    quantity: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The number of streaming distributions that were created by the current Amazon Web Services account. </p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.streaming_distribution_summary_list.StreamingDistributionSummaryList"
    ]
    """<p>A complex type that contains one <code>StreamingDistributionSummary</code> element for each distribution that was created by the current Amazon Web Services account.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StreamingDistributionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Marker").text = str(value["marker"])
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])
    SubElement(el, "IsTruncated").text = "true" if value["is_truncated"] else "false"
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import aws_sdk_cloudfront.types.streaming_distribution_summary_list

        aws_sdk_cloudfront.types.streaming_distribution_summary_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> StreamingDistributionList:
    out: StreamingDistributionList = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    else:
        raise DeserializationError("StreamingDistributionList.marker required")
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        raise DeserializationError("StreamingDistributionList.max_items required")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        raise DeserializationError("StreamingDistributionList.is_truncated required")
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("StreamingDistributionList.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.streaming_distribution_summary_list

        out["items"] = (
            aws_sdk_cloudfront.types.streaming_distribution_summary_list.deserialize_xml(
                child_items
            )
        )
    return out
