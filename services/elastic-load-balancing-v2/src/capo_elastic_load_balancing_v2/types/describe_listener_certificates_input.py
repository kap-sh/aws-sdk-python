"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeListenerCertificatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.listener_arn
    import capo_elastic_load_balancing_v2.types.marker
    import capo_elastic_load_balancing_v2.types.page_size


class DescribeListenerCertificatesInput(TypedDict, closed=True):
    listener_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
    ]
    """<p>The Amazon Resource Names (ARN) of the listener.</p>"""
    marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    page_size: NotRequired["capo_elastic_load_balancing_v2.types.page_size.PageSize"]
    """<p>The maximum number of results to return with this call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeListenerCertificatesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "listener_arn" in value:
        pairs.append((f"{key_prefix}ListenerArn", str(value["listener_arn"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "page_size" in value:
        pairs.append((f"{key_prefix}PageSize", str(value["page_size"])))


def deserialize_query(el: Element) -> DescribeListenerCertificatesInput:
    out: DescribeListenerCertificatesInput = {}  # type: ignore[typeddict-item]
    child_listener_arn = el.find("ListenerArn")
    if child_listener_arn is not None:
        out["listener_arn"] = str(child_listener_arn.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_page_size = el.find("PageSize")
    if child_page_size is not None:
        out["page_size"] = int(child_page_size.text or "")
    return out
