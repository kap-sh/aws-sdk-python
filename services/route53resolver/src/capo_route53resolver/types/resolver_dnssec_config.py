"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverDnssecConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.account_id
    import capo_route53resolver.types.resolver_dnssec_validation_status
    import capo_route53resolver.types.resource_id


class ResolverDnssecConfig(TypedDict, closed=True):
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID for a configuration for DNSSEC validation.</p>"""
    owner_id: NotRequired["capo_route53resolver.types.account_id.AccountId"]
    """<p>The owner account ID of the virtual private cloud (VPC) for a configuration for DNSSEC validation.</p>"""
    resource_id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the virtual private cloud (VPC) that you're configuring the DNSSEC validation status for.</p>"""
    validation_status: NotRequired[
        "capo_route53resolver.types.resolver_dnssec_validation_status.ResolverDNSSECValidationStatus"
    ]
    """<p>The validation status for a DNSSEC configuration. The status can be one of the following:</p> <ul> <li> <p> <b>ENABLING:</b> DNSSEC validation is being enabled but is not complete.</p> </li> <li> <p> <b>ENABLED:</b> DNSSEC validation is enabled.</p> </li> <li> <p> <b>DISABLING:</b> DNSSEC validation is being disabled but is not complete.</p> </li> <li> <p> <b>DISABLED</b> DNSSEC validation is disabled.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverDnssecConfig) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "validation_status" in value:
        import capo_route53resolver.types.resolver_dnssec_validation_status

        out["ValidationStatus"] = (
            capo_route53resolver.types.resolver_dnssec_validation_status.serialize_aws_json_1_1(
                value["validation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverDnssecConfig:
    out: ResolverDnssecConfig = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ValidationStatus" in data:
        import capo_route53resolver.types.resolver_dnssec_validation_status

        out["validation_status"] = (
            capo_route53resolver.types.resolver_dnssec_validation_status.deserialize_aws_json_1_1(
                data["ValidationStatus"]
            )
        )
    return out
