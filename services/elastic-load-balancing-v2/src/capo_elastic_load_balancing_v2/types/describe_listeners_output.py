"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeListenersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.listeners
    import capo_elastic_load_balancing_v2.types.marker


class DescribeListenersOutput(TypedDict, closed=True):
    listeners: NotRequired["capo_elastic_load_balancing_v2.types.listeners.Listeners"]
    """<p>Information about the listeners.</p>"""
    next_marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeListenersOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "listeners" in value:
        import capo_elastic_load_balancing_v2.types.listeners

        capo_elastic_load_balancing_v2.types.listeners.serialize_query(
            value["listeners"], pairs, f"{key_prefix}Listeners"
        )
    if "next_marker" in value:
        pairs.append((f"{key_prefix}NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeListenersOutput:
    out: DescribeListenersOutput = {}  # type: ignore[typeddict-item]
    child_listeners = el.find("Listeners")
    if child_listeners is not None:
        import capo_elastic_load_balancing_v2.types.listeners

        out["listeners"] = (
            capo_elastic_load_balancing_v2.types.listeners.deserialize_query(
                child_listeners
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
