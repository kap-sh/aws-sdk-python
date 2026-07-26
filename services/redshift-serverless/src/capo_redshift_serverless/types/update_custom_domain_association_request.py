"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateCustomDomainAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.custom_domain_certificate_arn_string
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.workgroup_name


class UpdateCustomDomainAssociationRequest(TypedDict, closed=True):
    workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup associated with the database.</p>"""
    custom_domain_name: (
        "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
    )
    """<p>The custom domain name associated with the workgroup.</p>"""
    custom_domain_certificate_arn: "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    """<p>The custom domain name’s certificate Amazon resource name (ARN). This is optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCustomDomainAssociationRequest) -> dict:
    out: dict = {}
    out["workgroupName"] = value["workgroup_name"]
    out["customDomainName"] = value["custom_domain_name"]
    out["customDomainCertificateArn"] = value["custom_domain_certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCustomDomainAssociationRequest:
    out: UpdateCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError(
            "UpdateCustomDomainAssociationRequest.workgroup_name required"
        )
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    else:
        raise DeserializationError(
            "UpdateCustomDomainAssociationRequest.custom_domain_name required"
        )
    if "customDomainCertificateArn" in data:
        out["custom_domain_certificate_arn"] = data["customDomainCertificateArn"]
    else:
        raise DeserializationError(
            "UpdateCustomDomainAssociationRequest.custom_domain_certificate_arn required"
        )
    return out
