"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeSSLPoliciesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.marker
    import capo_elastic_load_balancing_v2.types.ssl_policies


class DescribeSSLPoliciesOutput(TypedDict, closed=True):
    ssl_policies: NotRequired[
        "capo_elastic_load_balancing_v2.types.ssl_policies.SslPolicies"
    ]
    """<p>Information about the security policies.</p>"""
    next_marker: NotRequired["capo_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSSLPoliciesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ssl_policies" in value:
        import capo_elastic_load_balancing_v2.types.ssl_policies

        capo_elastic_load_balancing_v2.types.ssl_policies.serialize_query(
            value["ssl_policies"], pairs, f"{key_prefix}SslPolicies"
        )
    if "next_marker" in value:
        pairs.append((f"{key_prefix}NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeSSLPoliciesOutput:
    out: DescribeSSLPoliciesOutput = {}  # type: ignore[typeddict-item]
    child_ssl_policies = el.find("SslPolicies")
    if child_ssl_policies is not None:
        import capo_elastic_load_balancing_v2.types.ssl_policies

        out["ssl_policies"] = (
            capo_elastic_load_balancing_v2.types.ssl_policies.deserialize_query(
                child_ssl_policies
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
