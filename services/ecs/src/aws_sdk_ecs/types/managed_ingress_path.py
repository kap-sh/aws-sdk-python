"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedIngressPath``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.access_type
    import aws_sdk_ecs.types.managed_certificate
    import aws_sdk_ecs.types.managed_listener
    import aws_sdk_ecs.types.managed_listener_rule
    import aws_sdk_ecs.types.managed_load_balancer
    import aws_sdk_ecs.types.managed_security_groups
    import aws_sdk_ecs.types.managed_target_groups
    import aws_sdk_ecs.types.string


class ManagedIngressPath(TypedDict):
    access_type: "aws_sdk_ecs.types.access_type.AccessType"
    """<p>The type of access to the endpoint for the Express service.</p>"""
    endpoint: "aws_sdk_ecs.types.string.String"
    """<p>The endpoint for access to the Express service.</p>"""
    load_balancer: NotRequired[
        "aws_sdk_ecs.types.managed_load_balancer.ManagedLoadBalancer"
    ]
    """<p>The Application Load Balancer associated with the Express service.</p>"""
    load_balancer_security_groups: NotRequired[
        "aws_sdk_ecs.types.managed_security_groups.ManagedSecurityGroups"
    ]
    """<p>The security groups associated with the Application Load Balancer.</p>"""
    certificate: NotRequired["aws_sdk_ecs.types.managed_certificate.ManagedCertificate"]
    """<p>The ACM certificate for the Express service's domain.</p>"""
    listener: NotRequired["aws_sdk_ecs.types.managed_listener.ManagedListener"]
    """<p>The listeners associated with the Application Load Balancer.</p>"""
    rule: NotRequired["aws_sdk_ecs.types.managed_listener_rule.ManagedListenerRule"]
    """<p>The listener rules for the Application Load Balancer.</p>"""
    target_groups: NotRequired[
        "aws_sdk_ecs.types.managed_target_groups.ManagedTargetGroups"
    ]
    """<p>The target groups associated with the Application Load Balancer.</p>"""
