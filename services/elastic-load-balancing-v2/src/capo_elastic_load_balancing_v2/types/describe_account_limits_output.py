"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeAccountLimitsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.limits
    import capo_elastic_load_balancing_v2.types.marker


class DescribeAccountLimitsOutput(TypedDict, closed=True):
    limits: NotRequired["capo_elastic_load_balancing_v2.types.limits.Limits"]
    """<p>Information about the limits.</p>"""
    next_marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountLimitsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "limits" in value:
        import capo_elastic_load_balancing_v2.types.limits

        capo_elastic_load_balancing_v2.types.limits.serialize_query(
            value["limits"], pairs, f"{prefix}.Limits"
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeAccountLimitsOutput:
    out: DescribeAccountLimitsOutput = {}  # type: ignore[typeddict-item]
    child_limits = el.find("Limits")
    if child_limits is not None:
        import capo_elastic_load_balancing_v2.types.limits

        out["limits"] = capo_elastic_load_balancing_v2.types.limits.deserialize_query(
            child_limits
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
