"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceLoadBalancersDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsEcsServiceLoadBalancersDetails(TypedDict, closed=True):
    container_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the container to associate with the load balancer.</p>"""
    container_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The port on the container to associate with the load balancer. This port must correspond to a <code>containerPort</code> in the task definition the tasks in the service are using. For tasks that use the EC2 launch type, the container instance they are launched on must allow ingress traffic on the <code>hostPort</code> of the port mapping.</p>"""
    load_balancer_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the load balancer to associate with the Amazon ECS service or task set.</p> <p>Only specified when using a Classic Load Balancer. For an Application Load Balancer or a Network Load Balancer, the load balancer name is omitted.</p>"""
    target_group_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the Elastic Load Balancing target group or groups associated with a service or task set.</p> <p>Only specified when using an Application Load Balancer or a Network Load Balancer. For a Classic Load Balancer, the target group ARN is omitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceLoadBalancersDetails) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "container_port" in value:
        out["ContainerPort"] = value["container_port"]
    if "load_balancer_name" in value:
        out["LoadBalancerName"] = value["load_balancer_name"]
    if "target_group_arn" in value:
        out["TargetGroupArn"] = value["target_group_arn"]
    return out


def deserialize_json(data: dict) -> AwsEcsServiceLoadBalancersDetails:
    out: AwsEcsServiceLoadBalancersDetails = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    if "ContainerPort" in data:
        out["container_port"] = data["ContainerPort"]
    if "LoadBalancerName" in data:
        out["load_balancer_name"] = data["LoadBalancerName"]
    if "TargetGroupArn" in data:
        out["target_group_arn"] = data["TargetGroupArn"]
    return out
