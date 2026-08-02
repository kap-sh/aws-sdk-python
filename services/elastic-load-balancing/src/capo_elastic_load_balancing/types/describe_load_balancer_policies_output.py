"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeLoadBalancerPoliciesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.policy_descriptions


class DescribeLoadBalancerPoliciesOutput(TypedDict, closed=True):
    policy_descriptions: NotRequired[
        "capo_elastic_load_balancing.types.policy_descriptions.PolicyDescriptions"
    ]
    """<p>Information about the policies.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancerPoliciesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_descriptions" in value:
        import capo_elastic_load_balancing.types.policy_descriptions

        capo_elastic_load_balancing.types.policy_descriptions.serialize_query(
            value["policy_descriptions"], pairs, f"{key_prefix}PolicyDescriptions"
        )


def deserialize_query(el: Element) -> DescribeLoadBalancerPoliciesOutput:
    out: DescribeLoadBalancerPoliciesOutput = {}  # type: ignore[typeddict-item]
    child_policy_descriptions = el.find("PolicyDescriptions")
    if child_policy_descriptions is not None:
        import capo_elastic_load_balancing.types.policy_descriptions

        out["policy_descriptions"] = (
            capo_elastic_load_balancing.types.policy_descriptions.deserialize_query(
                child_policy_descriptions
            )
        )
    return out
