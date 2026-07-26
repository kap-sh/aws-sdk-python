"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeAccountLimitsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.limits
    import capo_elastic_load_balancing.types.marker


class DescribeAccountLimitsOutput(TypedDict, closed=True):
    limits: NotRequired["capo_elastic_load_balancing.types.limits.Limits"]
    """<p>Information about the limits.</p>"""
    next_marker: NotRequired["capo_elastic_load_balancing.types.marker.Marker"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountLimitsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "limits" in value:
        import capo_elastic_load_balancing.types.limits

        capo_elastic_load_balancing.types.limits.serialize_query(
            value["limits"], pairs, f"{prefix}.Limits"
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeAccountLimitsOutput:
    out: DescribeAccountLimitsOutput = {}  # type: ignore[typeddict-item]
    child_limits = el.find("Limits")
    if child_limits is not None:
        import capo_elastic_load_balancing.types.limits

        out["limits"] = capo_elastic_load_balancing.types.limits.deserialize_query(
            child_limits
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
