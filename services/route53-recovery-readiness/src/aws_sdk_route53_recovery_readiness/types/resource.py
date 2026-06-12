"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of__string
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.dns_target_resource


class Resource(TypedDict):
    component_id: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The component identifier of the resource, generated when DNS target resource is used.</p>"""
    dns_target_resource: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.dns_target_resource.DNSTargetResource"
    ]
    """<p>The DNS target resource.</p>"""
    readiness_scopes: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of recovery group Amazon Resource Names (ARNs) and cell ARNs that this resource is contained within.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "component_id" in value:
        out["componentId"] = value["component_id"]
    if "dns_target_resource" in value:
        import aws_sdk_route53_recovery_readiness.types.dns_target_resource

        out["dnsTargetResource"] = (
            aws_sdk_route53_recovery_readiness.types.dns_target_resource.serialize_json(
                value["dns_target_resource"]
            )
        )
    if "readiness_scopes" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of__string

        out["readinessScopes"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of__string.serialize_json(
                value["readiness_scopes"]
            )
        )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "componentId" in data:
        out["component_id"] = data["componentId"]
    if "dnsTargetResource" in data:
        import aws_sdk_route53_recovery_readiness.types.dns_target_resource

        out["dns_target_resource"] = (
            aws_sdk_route53_recovery_readiness.types.dns_target_resource.deserialize_json(
                data["dnsTargetResource"]
            )
        )
    if "readinessScopes" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of__string

        out["readiness_scopes"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of__string.deserialize_json(
                data["readinessScopes"]
            )
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    return out
