"""Generated from Smithy shape ``com.amazonaws.route53#GetHostedZoneLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.hosted_zone_limit
    import capo_route_53.types.usage_count


class GetHostedZoneLimitResponse(TypedDict, closed=True):
    limit: "capo_route_53.types.hosted_zone_limit.HostedZoneLimit"
    """<p>The current setting for the specified limit. For example, if you specified <code>MAX_RRSETS_BY_ZONE</code> for the value of <code>Type</code> in the request, the value of <code>Limit</code> is the maximum number of records that you can create in the specified hosted zone.</p>"""
    count: "capo_route_53.types.usage_count.UsageCount"
    """<p>The current number of entities that you have created of the specified type. For example, if you specified <code>MAX_RRSETS_BY_ZONE</code> for the value of <code>Type</code> in the request, the value of <code>Count</code> is the current number of records that you have created in the specified hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetHostedZoneLimitResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.hosted_zone_limit

    capo_route_53.types.hosted_zone_limit.serialize_xml(value["limit"], el, "Limit")
    SubElement(el, "Count").text = str(value.get("count", 0))


def deserialize_xml(el: Element) -> GetHostedZoneLimitResponse:
    out: GetHostedZoneLimitResponse = {}  # type: ignore[typeddict-item]
    child_limit = el.find("Limit")
    if child_limit is not None:
        import capo_route_53.types.hosted_zone_limit

        out["limit"] = capo_route_53.types.hosted_zone_limit.deserialize_xml(
            child_limit
        )
    else:
        raise DeserializationError("GetHostedZoneLimitResponse.limit required")
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    else:
        out["count"] = 0
    return out
