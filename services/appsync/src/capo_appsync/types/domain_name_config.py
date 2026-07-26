"""Generated from Smithy shape ``com.amazonaws.appsync#DomainNameConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.certificate_arn
    import capo_appsync.types.description
    import capo_appsync.types.domain_name
    import capo_appsync.types.string
    import capo_appsync.types.tag_map


class DomainNameConfig(TypedDict, closed=True):
    domain_name: NotRequired["capo_appsync.types.domain_name.DomainName"]
    """<p>The domain name.</p>"""
    description: NotRequired["capo_appsync.types.description.Description"]
    """<p>A description of the <code>DomainName</code> configuration.</p>"""
    certificate_arn: NotRequired["capo_appsync.types.certificate_arn.CertificateArn"]
    """<p>The Amazon Resource Name (ARN) of the certificate. This can be an Certificate Manager (ACM) certificate or an Identity and Access Management (IAM) server certificate.</p>"""
    appsync_domain_name: NotRequired["capo_appsync.types.string.String"]
    """<p>The domain name that AppSync provides.</p>"""
    hosted_zone_id: NotRequired["capo_appsync.types.string.String"]
    """<p>The ID of your Amazon Route 53 hosted zone.</p>"""
    tags: NotRequired["capo_appsync.types.tag_map.TagMap"]
    domain_name_arn: NotRequired["capo_appsync.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameConfig) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "appsync_domain_name" in value:
        out["appsyncDomainName"] = value["appsync_domain_name"]
    if "hosted_zone_id" in value:
        out["hostedZoneId"] = value["hosted_zone_id"]
    if "tags" in value:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.serialize_json(value["tags"])
    if "domain_name_arn" in value:
        out["domainNameArn"] = value["domain_name_arn"]
    return out


def deserialize_json(data: dict) -> DomainNameConfig:
    out: DomainNameConfig = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "description" in data:
        out["description"] = data["description"]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "appsyncDomainName" in data:
        out["appsync_domain_name"] = data["appsyncDomainName"]
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    if "tags" in data:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.deserialize_json(data["tags"])
    if "domainNameArn" in data:
        out["domain_name_arn"] = data["domainNameArn"]
    return out
