"""Generated from Smithy shape ``com.amazonaws.route53#ListTrafficPolicyVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.page_truncated
    import aws_sdk_route_53.types.traffic_policies
    import aws_sdk_route_53.types.traffic_policy_version_marker


class ListTrafficPolicyVersionsResponse(TypedDict):
    traffic_policies: "aws_sdk_route_53.types.traffic_policies.TrafficPolicies"
    """<p>A list that contains one <code>TrafficPolicy</code> element for each traffic policy version that is associated with the specified traffic policy.</p>"""
    is_truncated: "aws_sdk_route_53.types.page_truncated.PageTruncated"
    """<p>A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another <code>ListTrafficPolicyVersions</code> request and specifying the value of <code>NextMarker</code> in the <code>marker</code> parameter.</p>"""
    traffic_policy_version_marker: "aws_sdk_route_53.types.traffic_policy_version_marker.TrafficPolicyVersionMarker"
    """<p>If <code>IsTruncated</code> is <code>true</code>, the value of <code>TrafficPolicyVersionMarker</code> identifies the first traffic policy that Amazon Route 53 will return if you submit another request. Call <code>ListTrafficPolicyVersions</code> again and specify the value of <code>TrafficPolicyVersionMarker</code> in the <code>TrafficPolicyVersionMarker</code> request parameter.</p> <p>This element is present only if <code>IsTruncated</code> is <code>true</code>.</p>"""
    max_items: "int"
    """<p>The value that you specified for the <code>maxitems</code> parameter in the <code>ListTrafficPolicyVersions</code> request that produced the current response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListTrafficPolicyVersionsResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.traffic_policies

    aws_sdk_route_53.types.traffic_policies.serialize_xml(
        value["traffic_policies"], el, "TrafficPolicies"
    )
    SubElement(el, "IsTruncated").text = (
        "true" if value.get("is_truncated", False) else "false"
    )
    SubElement(el, "TrafficPolicyVersionMarker").text = str(
        value["traffic_policy_version_marker"]
    )
    SubElement(el, "MaxItems").text = str(value["max_items"])


def deserialize_xml(el: Element) -> ListTrafficPolicyVersionsResponse:
    out: ListTrafficPolicyVersionsResponse = {}  # type: ignore[typeddict-item]
    child_traffic_policies = el.find("TrafficPolicies")
    if child_traffic_policies is not None:
        import aws_sdk_route_53.types.traffic_policies

        out["traffic_policies"] = (
            aws_sdk_route_53.types.traffic_policies.deserialize_xml(
                child_traffic_policies
            )
        )
    else:
        raise DeserializationError(
            "ListTrafficPolicyVersionsResponse.traffic_policies required"
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_traffic_policy_version_marker = el.find("TrafficPolicyVersionMarker")
    if child_traffic_policy_version_marker is not None:
        out["traffic_policy_version_marker"] = str(
            child_traffic_policy_version_marker.text or ""
        )
    else:
        raise DeserializationError(
            "ListTrafficPolicyVersionsResponse.traffic_policy_version_marker required"
        )
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        raise DeserializationError(
            "ListTrafficPolicyVersionsResponse.max_items required"
        )
    return out
