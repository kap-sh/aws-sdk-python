"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByRealtimeLogConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListDistributionsByRealtimeLogConfigRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in your list of distributions. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of distributions that you want in the response.</p>"""
    realtime_log_config_name: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The name of the real-time log configuration whose associated distributions you want to list.</p>"""
    realtime_log_config_arn: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the real-time log configuration whose associated distributions you want to list.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByRealtimeLogConfigRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "marker" in value:
        SubElement(el, "Marker").text = str(value["marker"])
    if "max_items" in value:
        SubElement(el, "MaxItems").text = str(value["max_items"])
    if "realtime_log_config_name" in value:
        SubElement(el, "RealtimeLogConfigName").text = str(
            value["realtime_log_config_name"]
        )
    if "realtime_log_config_arn" in value:
        SubElement(el, "RealtimeLogConfigArn").text = str(
            value["realtime_log_config_arn"]
        )


def deserialize_xml(el: Element) -> ListDistributionsByRealtimeLogConfigRequest:
    out: ListDistributionsByRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    child_realtime_log_config_name = el.find("RealtimeLogConfigName")
    if child_realtime_log_config_name is not None:
        out["realtime_log_config_name"] = str(child_realtime_log_config_name.text or "")
    child_realtime_log_config_arn = el.find("RealtimeLogConfigArn")
    if child_realtime_log_config_arn is not None:
        out["realtime_log_config_arn"] = str(child_realtime_log_config_arn.text or "")
    return out
