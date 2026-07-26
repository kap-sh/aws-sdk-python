"""Generated from Smithy shape ``com.amazonaws.route53#GetReusableDelegationSetLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.reusable_delegation_set_limit
    import capo_route_53.types.usage_count


class GetReusableDelegationSetLimitResponse(TypedDict, closed=True):
    limit: (
        "capo_route_53.types.reusable_delegation_set_limit.ReusableDelegationSetLimit"
    )
    """<p>The current setting for the limit on hosted zones that you can associate with the specified reusable delegation set.</p>"""
    count: "capo_route_53.types.usage_count.UsageCount"
    """<p>The current number of hosted zones that you can associate with the specified reusable delegation set.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetReusableDelegationSetLimitResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.reusable_delegation_set_limit

    capo_route_53.types.reusable_delegation_set_limit.serialize_xml(
        value["limit"], el, "Limit"
    )
    SubElement(el, "Count").text = str(value.get("count", 0))


def deserialize_xml(el: Element) -> GetReusableDelegationSetLimitResponse:
    out: GetReusableDelegationSetLimitResponse = {}  # type: ignore[typeddict-item]
    child_limit = el.find("Limit")
    if child_limit is not None:
        import capo_route_53.types.reusable_delegation_set_limit

        out["limit"] = (
            capo_route_53.types.reusable_delegation_set_limit.deserialize_xml(
                child_limit
            )
        )
    else:
        raise DeserializationError(
            "GetReusableDelegationSetLimitResponse.limit required"
        )
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    else:
        out["count"] = 0
    return out
