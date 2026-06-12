"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#TargetResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.nlb_resource
    import aws_sdk_route53_recovery_readiness.types.r53_resource_record


class TargetResource(TypedDict):
    nlb_resource: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.nlb_resource.NLBResource"
    ]
    """<p>The Network Load Balancer Resource.</p>"""
    r53_resource: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.r53_resource_record.R53ResourceRecord"
    ]
    """<p>The Route 53 resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetResource) -> dict:
    out: dict = {}
    if "nlb_resource" in value:
        import aws_sdk_route53_recovery_readiness.types.nlb_resource

        out["nLBResource"] = (
            aws_sdk_route53_recovery_readiness.types.nlb_resource.serialize_json(
                value["nlb_resource"]
            )
        )
    if "r53_resource" in value:
        import aws_sdk_route53_recovery_readiness.types.r53_resource_record

        out["r53Resource"] = (
            aws_sdk_route53_recovery_readiness.types.r53_resource_record.serialize_json(
                value["r53_resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> TargetResource:
    out: TargetResource = {}  # type: ignore[typeddict-item]
    if "nLBResource" in data:
        import aws_sdk_route53_recovery_readiness.types.nlb_resource

        out["nlb_resource"] = (
            aws_sdk_route53_recovery_readiness.types.nlb_resource.deserialize_json(
                data["nLBResource"]
            )
        )
    if "r53Resource" in data:
        import aws_sdk_route53_recovery_readiness.types.r53_resource_record

        out["r53_resource"] = (
            aws_sdk_route53_recovery_readiness.types.r53_resource_record.deserialize_json(
                data["r53Resource"]
            )
        )
    return out
