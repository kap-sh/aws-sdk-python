"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.marker
    import capo_elastic_load_balancing_v2.types.rules


class DescribeRulesOutput(TypedDict, closed=True):
    rules: NotRequired["capo_elastic_load_balancing_v2.types.rules.Rules"]
    """<p>Information about the rules.</p>"""
    next_marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rules" in value:
        import capo_elastic_load_balancing_v2.types.rules

        capo_elastic_load_balancing_v2.types.rules.serialize_query(
            value["rules"], pairs, f"{key_prefix}Rules"
        )
    if "next_marker" in value:
        pairs.append((f"{key_prefix}NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeRulesOutput:
    out: DescribeRulesOutput = {}  # type: ignore[typeddict-item]
    child_rules = el.find("Rules")
    if child_rules is not None:
        import capo_elastic_load_balancing_v2.types.rules

        out["rules"] = capo_elastic_load_balancing_v2.types.rules.deserialize_query(
            child_rules
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
