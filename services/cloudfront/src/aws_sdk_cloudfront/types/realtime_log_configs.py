"""Generated from Smithy shape ``com.amazonaws.cloudfront#RealtimeLogConfigs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.realtime_log_config_list
    import aws_sdk_cloudfront.types.string


class RealtimeLogConfigs(TypedDict, closed=True):
    max_items: "aws_sdk_cloudfront.types.integer.integer"
    """<p>The maximum number of real-time log configurations requested.</p>"""
    items: NotRequired[
        "aws_sdk_cloudfront.types.realtime_log_config_list.RealtimeLogConfigList"
    ]
    """<p>Contains the list of real-time log configurations.</p>"""
    is_truncated: "aws_sdk_cloudfront.types.boolean.boolean"
    """<p>A flag that indicates whether there are more real-time log configurations than are contained in this list.</p>"""
    marker: "aws_sdk_cloudfront.types.string.string"
    """<p>This parameter indicates where this list of real-time log configurations begins. This list includes real-time log configurations that occur after the marker.</p>"""
    next_marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the <code>Marker</code> field of a subsequent request to continue listing real-time log configurations where you left off. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: RealtimeLogConfigs, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "MaxItems").text = str(value["max_items"])
    if "items" in value:
        import aws_sdk_cloudfront.types.realtime_log_config_list

        aws_sdk_cloudfront.types.realtime_log_config_list.serialize_xml(
            value["items"], el, "Items"
        )
    SubElement(el, "IsTruncated").text = "true" if value["is_truncated"] else "false"
    SubElement(el, "Marker").text = str(value["marker"])
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])


def deserialize_xml(el: Element) -> RealtimeLogConfigs:
    out: RealtimeLogConfigs = {}  # type: ignore[typeddict-item]
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        raise DeserializationError("RealtimeLogConfigs.max_items required")
    child_items = el.find("Items")
    if child_items is not None:
        import aws_sdk_cloudfront.types.realtime_log_config_list

        out["items"] = (
            aws_sdk_cloudfront.types.realtime_log_config_list.deserialize_xml(
                child_items
            )
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        raise DeserializationError("RealtimeLogConfigs.is_truncated required")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    else:
        raise DeserializationError("RealtimeLogConfigs.marker required")
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
