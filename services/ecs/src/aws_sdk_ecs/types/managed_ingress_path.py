"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedIngressPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.access_type
    import aws_sdk_ecs.types.managed_certificate
    import aws_sdk_ecs.types.managed_listener
    import aws_sdk_ecs.types.managed_listener_rule
    import aws_sdk_ecs.types.managed_load_balancer
    import aws_sdk_ecs.types.managed_security_groups
    import aws_sdk_ecs.types.managed_target_groups
    import aws_sdk_ecs.types.string


class ManagedIngressPath(TypedDict, closed=True):
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedIngressPath) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.access_type

    out["accessType"] = aws_sdk_ecs.types.access_type.serialize_aws_json_1_1(
        value["access_type"]
    )
    out["endpoint"] = value["endpoint"]
    if "load_balancer" in value:
        import aws_sdk_ecs.types.managed_load_balancer

        out["loadBalancer"] = (
            aws_sdk_ecs.types.managed_load_balancer.serialize_aws_json_1_1(
                value["load_balancer"]
            )
        )
    if "load_balancer_security_groups" in value:
        import aws_sdk_ecs.types.managed_security_groups

        out["loadBalancerSecurityGroups"] = (
            aws_sdk_ecs.types.managed_security_groups.serialize_aws_json_1_1(
                value["load_balancer_security_groups"]
            )
        )
    if "certificate" in value:
        import aws_sdk_ecs.types.managed_certificate

        out["certificate"] = (
            aws_sdk_ecs.types.managed_certificate.serialize_aws_json_1_1(
                value["certificate"]
            )
        )
    if "listener" in value:
        import aws_sdk_ecs.types.managed_listener

        out["listener"] = aws_sdk_ecs.types.managed_listener.serialize_aws_json_1_1(
            value["listener"]
        )
    if "rule" in value:
        import aws_sdk_ecs.types.managed_listener_rule

        out["rule"] = aws_sdk_ecs.types.managed_listener_rule.serialize_aws_json_1_1(
            value["rule"]
        )
    if "target_groups" in value:
        import aws_sdk_ecs.types.managed_target_groups

        out["targetGroups"] = (
            aws_sdk_ecs.types.managed_target_groups.serialize_aws_json_1_1(
                value["target_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedIngressPath:
    out: ManagedIngressPath = {}  # type: ignore[typeddict-item]
    if "accessType" in data:
        import aws_sdk_ecs.types.access_type

        out["access_type"] = aws_sdk_ecs.types.access_type.deserialize_aws_json_1_1(
            data["accessType"]
        )
    else:
        raise DeserializationError("ManagedIngressPath.access_type required")
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("ManagedIngressPath.endpoint required")
    if "loadBalancer" in data:
        import aws_sdk_ecs.types.managed_load_balancer

        out["load_balancer"] = (
            aws_sdk_ecs.types.managed_load_balancer.deserialize_aws_json_1_1(
                data["loadBalancer"]
            )
        )
    if "loadBalancerSecurityGroups" in data:
        import aws_sdk_ecs.types.managed_security_groups

        out["load_balancer_security_groups"] = (
            aws_sdk_ecs.types.managed_security_groups.deserialize_aws_json_1_1(
                data["loadBalancerSecurityGroups"]
            )
        )
    if "certificate" in data:
        import aws_sdk_ecs.types.managed_certificate

        out["certificate"] = (
            aws_sdk_ecs.types.managed_certificate.deserialize_aws_json_1_1(
                data["certificate"]
            )
        )
    if "listener" in data:
        import aws_sdk_ecs.types.managed_listener

        out["listener"] = aws_sdk_ecs.types.managed_listener.deserialize_aws_json_1_1(
            data["listener"]
        )
    if "rule" in data:
        import aws_sdk_ecs.types.managed_listener_rule

        out["rule"] = aws_sdk_ecs.types.managed_listener_rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    if "targetGroups" in data:
        import aws_sdk_ecs.types.managed_target_groups

        out["target_groups"] = (
            aws_sdk_ecs.types.managed_target_groups.deserialize_aws_json_1_1(
                data["targetGroups"]
            )
        )
    return out
