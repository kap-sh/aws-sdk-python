"""Generated from Smithy shape ``com.amazonaws.appsync#CreateDomainNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.certificate_arn
    import capo_appsync.types.description
    import capo_appsync.types.domain_name
    import capo_appsync.types.tag_map


class CreateDomainNameRequest(TypedDict, closed=True):
    domain_name: "capo_appsync.types.domain_name.DomainName"
    """<p>The domain name.</p>"""
    certificate_arn: "capo_appsync.types.certificate_arn.CertificateArn"
    """<p>The Amazon Resource Name (ARN) of the certificate. This can be an Certificate Manager (ACM) certificate or an Identity and Access Management (IAM) server certificate.</p>"""
    description: NotRequired["capo_appsync.types.description.Description"]
    """<p>A description of the <code>DomainName</code>.</p>"""
    tags: NotRequired["capo_appsync.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainNameRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    out["certificateArn"] = value["certificate_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDomainNameRequest:
    out: CreateDomainNameRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("CreateDomainNameRequest.domain_name required")
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    else:
        raise DeserializationError("CreateDomainNameRequest.certificate_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.deserialize_json(data["tags"])
    return out
