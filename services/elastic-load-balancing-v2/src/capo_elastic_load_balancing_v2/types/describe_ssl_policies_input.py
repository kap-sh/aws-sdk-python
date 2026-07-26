"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeSSLPoliciesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.load_balancer_type_enum
    import capo_elastic_load_balancing_v2.types.marker
    import capo_elastic_load_balancing_v2.types.page_size
    import capo_elastic_load_balancing_v2.types.ssl_policy_names


class DescribeSSLPoliciesInput(TypedDict, closed=True):
    names: NotRequired[
        "capo_elastic_load_balancing_v2.types.ssl_policy_names.SslPolicyNames"
    ]
    """<p>The names of the policies.</p>"""
    marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["capo_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""
    load_balancer_type: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_type_enum.LoadBalancerTypeEnum"
    ]
    """<p> The type of load balancer. The default lists the SSL policies for all load balancers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSSLPoliciesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "names" in value:
        import capo_elastic_load_balancing_v2.types.ssl_policy_names

        capo_elastic_load_balancing_v2.types.ssl_policy_names.serialize_query(
            value["names"], pairs, f"{prefix}.Names"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{prefix}.PageSize", str(value["page_size"])))
    if "load_balancer_type" in value:
        import capo_elastic_load_balancing_v2.types.load_balancer_type_enum

        capo_elastic_load_balancing_v2.types.load_balancer_type_enum.serialize_query(
            value["load_balancer_type"], pairs, f"{prefix}.LoadBalancerType"
        )


def deserialize_query(el: Element) -> DescribeSSLPoliciesInput:
    out: DescribeSSLPoliciesInput = {}  # type: ignore[typeddict-item]
    child_names = el.find("Names")
    if child_names is not None:
        import capo_elastic_load_balancing_v2.types.ssl_policy_names

        out["names"] = (
            capo_elastic_load_balancing_v2.types.ssl_policy_names.deserialize_query(
                child_names
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    child_load_balancer_type = el.find("LoadBalancerType")
    if child_load_balancer_type is not None:
        import capo_elastic_load_balancing_v2.types.load_balancer_type_enum

        out["load_balancer_type"] = (
            capo_elastic_load_balancing_v2.types.load_balancer_type_enum.deserialize_query(
                child_load_balancer_type
            )
        )
    return out
