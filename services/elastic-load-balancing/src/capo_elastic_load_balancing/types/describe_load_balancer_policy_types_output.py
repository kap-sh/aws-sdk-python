"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeLoadBalancerPolicyTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.policy_type_descriptions


class DescribeLoadBalancerPolicyTypesOutput(TypedDict, closed=True):
    policy_type_descriptions: NotRequired[
        "capo_elastic_load_balancing.types.policy_type_descriptions.PolicyTypeDescriptions"
    ]
    """<p>Information about the policy types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancerPolicyTypesOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "policy_type_descriptions" in value:
        import capo_elastic_load_balancing.types.policy_type_descriptions

        capo_elastic_load_balancing.types.policy_type_descriptions.serialize_query(
            value["policy_type_descriptions"],
            pairs,
            f"{key_prefix}PolicyTypeDescriptions",
        )


def deserialize_query(el: Element) -> DescribeLoadBalancerPolicyTypesOutput:
    out: DescribeLoadBalancerPolicyTypesOutput = {}  # type: ignore[typeddict-item]
    child_policy_type_descriptions = el.find("PolicyTypeDescriptions")
    if child_policy_type_descriptions is not None:
        import capo_elastic_load_balancing.types.policy_type_descriptions

        out["policy_type_descriptions"] = (
            capo_elastic_load_balancing.types.policy_type_descriptions.deserialize_query(
                child_policy_type_descriptions
            )
        )
    return out
