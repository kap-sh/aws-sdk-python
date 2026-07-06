"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeLoadBalancerPolicyTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.policy_type_names


class DescribeLoadBalancerPolicyTypesInput(TypedDict, closed=True):
    policy_type_names: NotRequired[
        "aws_sdk_elastic_load_balancing.types.policy_type_names.PolicyTypeNames"
    ]
    """<p>The names of the policy types. If no names are specified, describes all policy types defined by Elastic Load Balancing.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeLoadBalancerPolicyTypesInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "policy_type_names" in value:
        import aws_sdk_elastic_load_balancing.types.policy_type_names

        aws_sdk_elastic_load_balancing.types.policy_type_names.serialize_query(
            value["policy_type_names"], pairs, f"{prefix}.PolicyTypeNames"
        )


def deserialize_query(el: Element) -> DescribeLoadBalancerPolicyTypesInput:
    out: DescribeLoadBalancerPolicyTypesInput = {}  # type: ignore[typeddict-item]
    child_policy_type_names = el.find("PolicyTypeNames")
    if child_policy_type_names is not None:
        import aws_sdk_elastic_load_balancing.types.policy_type_names

        out["policy_type_names"] = (
            aws_sdk_elastic_load_balancing.types.policy_type_names.deserialize_query(
                child_policy_type_names
            )
        )
    return out
