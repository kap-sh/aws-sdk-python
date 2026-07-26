"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeAccessPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.load_balancer_names
    import capo_elastic_load_balancing.types.marker
    import capo_elastic_load_balancing.types.page_size


class DescribeAccessPointsInput(TypedDict, closed=True):
    load_balancer_names: NotRequired[
        "capo_elastic_load_balancing.types.load_balancer_names.LoadBalancerNames"
    ]
    """<p>The names of the load balancers.</p>"""
    marker: NotRequired["capo_elastic_load_balancing.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["capo_elastic_load_balancing.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call (a number from 1 to 400). The default is 400.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccessPointsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_names" in value:
        import capo_elastic_load_balancing.types.load_balancer_names

        capo_elastic_load_balancing.types.load_balancer_names.serialize_query(
            value["load_balancer_names"], pairs, f"{prefix}.LoadBalancerNames"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{prefix}.PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeAccessPointsInput:
    out: DescribeAccessPointsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_names = el.find("LoadBalancerNames")
    if child_load_balancer_names is not None:
        import capo_elastic_load_balancing.types.load_balancer_names

        out["load_balancer_names"] = (
            capo_elastic_load_balancing.types.load_balancer_names.deserialize_query(
                child_load_balancer_names
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
