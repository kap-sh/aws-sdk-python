"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#DNSTargetResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.target_resource


class DNSTargetResource(TypedDict, closed=True):
    domain_name: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The domain name that acts as an ingress point to a portion of the customer application.</p>"""
    hosted_zone_arn: NotRequired[
        "capo_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The hosted zone Amazon Resource Name (ARN) that contains the DNS record with the provided name of the target resource.</p>"""
    record_set_id: NotRequired[
        "capo_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The Route 53 record set ID that uniquely identifies a DNS record, given a name and a type.</p>"""
    record_type: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The type of DNS record of the target resource.</p>"""
    target_resource: NotRequired[
        "capo_route53_recovery_readiness.types.target_resource.TargetResource"
    ]
    """<p>The target resource of the DNS target resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DNSTargetResource) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "hosted_zone_arn" in value:
        out["hostedZoneArn"] = value["hosted_zone_arn"]
    if "record_set_id" in value:
        out["recordSetId"] = value["record_set_id"]
    if "record_type" in value:
        out["recordType"] = value["record_type"]
    if "target_resource" in value:
        import capo_route53_recovery_readiness.types.target_resource

        out["targetResource"] = (
            capo_route53_recovery_readiness.types.target_resource.serialize_json(
                value["target_resource"]
            )
        )
    return out


def deserialize_json(data: dict) -> DNSTargetResource:
    out: DNSTargetResource = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "hostedZoneArn" in data:
        out["hosted_zone_arn"] = data["hostedZoneArn"]
    if "recordSetId" in data:
        out["record_set_id"] = data["recordSetId"]
    if "recordType" in data:
        out["record_type"] = data["recordType"]
    if "targetResource" in data:
        import capo_route53_recovery_readiness.types.target_resource

        out["target_resource"] = (
            capo_route53_recovery_readiness.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    return out
