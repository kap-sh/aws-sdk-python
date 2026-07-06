"""Generated from Smithy shape ``com.amazonaws.route53#ListHealthChecksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_checks
    import aws_sdk_route_53.types.page_marker
    import aws_sdk_route_53.types.page_truncated


class ListHealthChecksResponse(TypedDict, closed=True):
    health_checks: "aws_sdk_route_53.types.health_checks.HealthChecks"
    """<p>A complex type that contains one <code>HealthCheck</code> element for each health check that is associated with the current Amazon Web Services account.</p>"""
    marker: "aws_sdk_route_53.types.page_marker.PageMarker"
    """<p>For the second and subsequent calls to <code>ListHealthChecks</code>, <code>Marker</code> is the value that you specified for the <code>marker</code> parameter in the previous request.</p>"""
    is_truncated: "aws_sdk_route_53.types.page_truncated.PageTruncated"
    """<p>A flag that indicates whether there are more health checks to be listed. If the response was truncated, you can get the next group of health checks by submitting another <code>ListHealthChecks</code> request and specifying the value of <code>NextMarker</code> in the <code>marker</code> parameter.</p>"""
    next_marker: NotRequired["aws_sdk_route_53.types.page_marker.PageMarker"]
    """<p>If <code>IsTruncated</code> is <code>true</code>, the value of <code>NextMarker</code> identifies the first health check that Amazon Route 53 returns if you submit another <code>ListHealthChecks</code> request and specify the value of <code>NextMarker</code> in the <code>marker</code> parameter.</p>"""
    max_items: "int"
    """<p>The value that you specified for the <code>maxitems</code> parameter in the call to <code>ListHealthChecks</code> that produced the current response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListHealthChecksResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.health_checks

    aws_sdk_route_53.types.health_checks.serialize_xml(
        value["health_checks"], el, "HealthChecks"
    )
    SubElement(el, "Marker").text = str(value["marker"])
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListHealthChecksResponse:
    out: ListHealthChecksResponse = {}  # type: ignore[typeddict-item]
    child_health_checks = el.find("HealthChecks")
    if child_health_checks is not None:
        import aws_sdk_route_53.types.health_checks

        out["health_checks"] = aws_sdk_route_53.types.health_checks.deserialize_xml(
            child_health_checks
        )
    else:
        raise DeserializationError("ListHealthChecksResponse.health_checks required")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    else:
        raise DeserializationError("ListHealthChecksResponse.marker required")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        raise DeserializationError("ListHealthChecksResponse.max_items required")
    return out
