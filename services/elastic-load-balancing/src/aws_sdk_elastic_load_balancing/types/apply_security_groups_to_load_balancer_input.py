"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ApplySecurityGroupsToLoadBalancerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.security_groups


class ApplySecurityGroupsToLoadBalancerInput(TypedDict, closed=True):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    security_groups: (
        "aws_sdk_elastic_load_balancing.types.security_groups.SecurityGroups"
    )
    """<p>The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplySecurityGroupsToLoadBalancerInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    import aws_sdk_elastic_load_balancing.types.security_groups

    aws_sdk_elastic_load_balancing.types.security_groups.serialize_query(
        value["security_groups"], pairs, f"{prefix}.SecurityGroups"
    )


def deserialize_query(el: Element) -> ApplySecurityGroupsToLoadBalancerInput:
    out: ApplySecurityGroupsToLoadBalancerInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "ApplySecurityGroupsToLoadBalancerInput.load_balancer_name required"
        )
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import aws_sdk_elastic_load_balancing.types.security_groups

        out["security_groups"] = (
            aws_sdk_elastic_load_balancing.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    else:
        raise DeserializationError(
            "ApplySecurityGroupsToLoadBalancerInput.security_groups required"
        )
    return out
