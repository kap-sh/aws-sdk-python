"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Association``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.custom_domain_certificate_arn_string
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.workgroup_name


class Association(TypedDict, closed=True):
    custom_domain_certificate_arn: NotRequired[
        "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    ]
    """<p>The custom domain name’s certificate Amazon resource name (ARN).</p>"""
    custom_domain_certificate_expiry_time: NotRequired["datetime.datetime"]
    """<p>The expiration time for the certificate.</p>"""
    custom_domain_name: NotRequired[
        "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
    ]
    """<p>The custom domain name associated with the workgroup.</p>"""
    workgroup_name: NotRequired[
        "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    ]
    """<p>The name of the workgroup associated with the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Association) -> dict:
    out: dict = {}
    if "custom_domain_certificate_arn" in value:
        out["customDomainCertificateArn"] = value["custom_domain_certificate_arn"]
    if "custom_domain_certificate_expiry_time" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        out["customDomainCertificateExpiryTime"] = (
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["custom_domain_certificate_expiry_time"]
            )
        )
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Association:
    out: Association = {}  # type: ignore[typeddict-item]
    if "customDomainCertificateArn" in data:
        out["custom_domain_certificate_arn"] = data["customDomainCertificateArn"]
    if "customDomainCertificateExpiryTime" in data:
        import capo_redshift_serverless.types._prelude.timestamp

        out["custom_domain_certificate_expiry_time"] = (
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["customDomainCertificateExpiryTime"]
            )
        )
    if "customDomainName" in data:
        out["custom_domain_name"] = data["customDomainName"]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    return out
