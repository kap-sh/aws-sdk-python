"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateCustomDomainAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.custom_domain_certificate_arn_string
    import aws_sdk_redshift_serverless.types.custom_domain_name
    import aws_sdk_redshift_serverless.types.workgroup_name


class CreateCustomDomainAssociationRequest(TypedDict):
    workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup associated with the database.</p>"""
    custom_domain_name: (
        "aws_sdk_redshift_serverless.types.custom_domain_name.CustomDomainName"
    )
    """<p>The custom domain name to associate with the workgroup.</p>"""
    custom_domain_certificate_arn: "aws_sdk_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    """<p>The custom domain name’s certificate Amazon resource name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomDomainAssociationRequest) -> dict:
    out: dict = {}
    out["workgroupName"] = value["workgroup_name"]
    out["customDomainName"] = value["custom_domain_name"]
    out["customDomainCertificateArn"] = value["custom_domain_certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomDomainAssociationRequest:
    out: CreateCustomDomainAssociationRequest = {}  # type: ignore[typeddict-item]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError(
            "CreateCustomDomainAssociationRequest.workgroup_name required"
        )
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    else:
        raise DeserializationError(
            "CreateCustomDomainAssociationRequest.custom_domain_name required"
        )
    if "customDomainCertificateArn" in data:
        out["custom_domain_certificate_arn"] = data["customDomainCertificateArn"]
    else:
        raise DeserializationError(
            "CreateCustomDomainAssociationRequest.custom_domain_certificate_arn required"
        )
    return out
