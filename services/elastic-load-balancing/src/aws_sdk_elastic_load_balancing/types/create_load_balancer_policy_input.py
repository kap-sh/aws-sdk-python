"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLoadBalancerPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.policy_attributes
    import aws_sdk_elastic_load_balancing.types.policy_name
    import aws_sdk_elastic_load_balancing.types.policy_type_name


class CreateLoadBalancerPolicyInput(TypedDict):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    policy_name: "aws_sdk_elastic_load_balancing.types.policy_name.PolicyName"
    """<p>The name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.</p>"""
    policy_type_name: (
        "aws_sdk_elastic_load_balancing.types.policy_type_name.PolicyTypeName"
    )
    """<p>The name of the base policy type. To get the list of policy types, use <a>DescribeLoadBalancerPolicyTypes</a>.</p>"""
    policy_attributes: NotRequired[
        "aws_sdk_elastic_load_balancing.types.policy_attributes.PolicyAttributes"
    ]
    """<p>The policy attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLoadBalancerPolicyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    pairs.append((f"{prefix}.PolicyTypeName", str(value["policy_type_name"])))
    if "policy_attributes" in value:
        import aws_sdk_elastic_load_balancing.types.policy_attributes

        aws_sdk_elastic_load_balancing.types.policy_attributes.serialize_query(
            value["policy_attributes"], pairs, f"{prefix}.PolicyAttributes"
        )


def deserialize_query(el: Element) -> CreateLoadBalancerPolicyInput:
    out: CreateLoadBalancerPolicyInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "CreateLoadBalancerPolicyInput.load_balancer_name required"
        )
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    else:
        raise DeserializationError("CreateLoadBalancerPolicyInput.policy_name required")
    child_policy_type_name = el.find("PolicyTypeName")
    if child_policy_type_name is not None:
        out["policy_type_name"] = str(child_policy_type_name.text or "")
    else:
        raise DeserializationError(
            "CreateLoadBalancerPolicyInput.policy_type_name required"
        )
    child_policy_attributes = el.find("PolicyAttributes")
    if child_policy_attributes is not None:
        import aws_sdk_elastic_load_balancing.types.policy_attributes

        out["policy_attributes"] = (
            aws_sdk_elastic_load_balancing.types.policy_attributes.deserialize_query(
                child_policy_attributes
            )
        )
    return out
