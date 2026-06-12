"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SetLoadBalancerPoliciesForBackendServerInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.end_point_port
    import aws_sdk_elastic_load_balancing.types.policy_names


class SetLoadBalancerPoliciesForBackendServerInput(TypedDict):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    instance_port: "aws_sdk_elastic_load_balancing.types.end_point_port.EndPointPort"
    """<p>The port number associated with the EC2 instance.</p>"""
    policy_names: "aws_sdk_elastic_load_balancing.types.policy_names.PolicyNames"
    """<p>The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetLoadBalancerPoliciesForBackendServerInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    pairs.append((f"{prefix}.InstancePort", str(value["instance_port"])))
    import aws_sdk_elastic_load_balancing.types.policy_names

    aws_sdk_elastic_load_balancing.types.policy_names.serialize_query(
        value["policy_names"], pairs, f"{prefix}.PolicyNames"
    )


def deserialize_query(el: Element) -> SetLoadBalancerPoliciesForBackendServerInput:
    out: SetLoadBalancerPoliciesForBackendServerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "SetLoadBalancerPoliciesForBackendServerInput.load_balancer_name required"
        )
    child_instance_port = el.find("InstancePort")
    if child_instance_port is not None:
        out["instance_port"] = int(child_instance_port.text or "")
    else:
        raise DeserializationError(
            "SetLoadBalancerPoliciesForBackendServerInput.instance_port required"
        )
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import aws_sdk_elastic_load_balancing.types.policy_names

        out["policy_names"] = (
            aws_sdk_elastic_load_balancing.types.policy_names.deserialize_query(
                child_policy_names
            )
        )
    else:
        raise DeserializationError(
            "SetLoadBalancerPoliciesForBackendServerInput.policy_names required"
        )
    return out
