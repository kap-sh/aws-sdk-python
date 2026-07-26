"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeTrafficSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.traffic_source_states
    import capo_auto_scaling.types.xml_string


class DescribeTrafficSourcesResponse(TypedDict, closed=True):
    traffic_sources: NotRequired[
        "capo_auto_scaling.types.traffic_source_states.TrafficSourceStates"
    ]
    """<p>Information about the traffic sources.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>This string indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTrafficSourcesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_sources" in value:
        import capo_auto_scaling.types.traffic_source_states

        capo_auto_scaling.types.traffic_source_states.serialize_query(
            value["traffic_sources"], pairs, f"{prefix}.TrafficSources"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeTrafficSourcesResponse:
    out: DescribeTrafficSourcesResponse = {}  # type: ignore[typeddict-item]
    child_traffic_sources = el.find("TrafficSources")
    if child_traffic_sources is not None:
        import capo_auto_scaling.types.traffic_source_states

        out["traffic_sources"] = (
            capo_auto_scaling.types.traffic_source_states.deserialize_query(
                child_traffic_sources
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
