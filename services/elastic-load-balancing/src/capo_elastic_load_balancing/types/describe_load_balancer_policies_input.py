"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeLoadBalancerPoliciesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.access_point_name
    import capo_elastic_load_balancing.types.policy_names


class DescribeLoadBalancerPoliciesInput(TypedDict, closed=True):
    load_balancer_name: NotRequired[
        "capo_elastic_load_balancing.types.access_point_name.AccessPointName"
    ]
    """<p>The name of the load balancer.</p>"""
    policy_names: NotRequired[
        "capo_elastic_load_balancing.types.policy_names.PolicyNames"
    ]
    """<p>The names of the policies.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancerPoliciesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_name" in value:
        pairs.append(
            (f"{key_prefix}LoadBalancerName", str(value["load_balancer_name"]))
        )
    if "policy_names" in value:
        import capo_elastic_load_balancing.types.policy_names

        capo_elastic_load_balancing.types.policy_names.serialize_query(
            value["policy_names"], pairs, f"{key_prefix}PolicyNames"
        )


def deserialize_query(el: Element) -> DescribeLoadBalancerPoliciesInput:
    out: DescribeLoadBalancerPoliciesInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import capo_elastic_load_balancing.types.policy_names

        out["policy_names"] = (
            capo_elastic_load_balancing.types.policy_names.deserialize_query(
                child_policy_names
            )
        )
    return out
