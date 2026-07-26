"""Generated from Smithy shape ``com.amazonaws.route53#GetAccountLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.account_limit
    import capo_route_53.types.usage_count


class GetAccountLimitResponse(TypedDict, closed=True):
    limit: "capo_route_53.types.account_limit.AccountLimit"
    """<p>The current setting for the specified limit. For example, if you specified <code>MAX_HEALTH_CHECKS_BY_OWNER</code> for the value of <code>Type</code> in the request, the value of <code>Limit</code> is the maximum number of health checks that you can create using the current account.</p>"""
    count: "capo_route_53.types.usage_count.UsageCount"
    """<p>The current number of entities that you have created of the specified type. For example, if you specified <code>MAX_HEALTH_CHECKS_BY_OWNER</code> for the value of <code>Type</code> in the request, the value of <code>Count</code> is the current number of health checks that you have created using the current account.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetAccountLimitResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.account_limit

    capo_route_53.types.account_limit.serialize_xml(value["limit"], el, "Limit")
    SubElement(el, "Count").text = str(value.get("count", 0))


def deserialize_xml(el: Element) -> GetAccountLimitResponse:
    out: GetAccountLimitResponse = {}  # type: ignore[typeddict-item]
    child_limit = el.find("Limit")
    if child_limit is not None:
        import capo_route_53.types.account_limit

        out["limit"] = capo_route_53.types.account_limit.deserialize_xml(child_limit)
    else:
        raise DeserializationError("GetAccountLimitResponse.limit required")
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    else:
        out["count"] = 0
    return out
