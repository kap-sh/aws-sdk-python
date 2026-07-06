"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionViewerCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsCloudFrontDistributionViewerCertificate(TypedDict, closed=True):
    acm_certificate_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the ACM certificate. Used if the certificate is stored in ACM. If you provide an ACM certificate ARN, you must also provide <code>MinimumCertificateVersion</code> and <code>SslSupportMethod</code>.</p>"""
    certificate: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the certificate. Note that in CloudFront, this attribute is deprecated.</p>"""
    certificate_source: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The source of the certificate identified by <code>Certificate</code>. Note that in CloudFront, this attribute is deprecated.</p>"""
    cloud_front_default_certificate: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether the distribution uses the CloudFront domain name. If set to <code>false</code>, then you provide either <code>AcmCertificateArn</code> or <code>IamCertificateId</code>.</p>"""
    iam_certificate_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the IAM certificate. Used if the certificate is stored in IAM. If you provide <code>IamCertificateId</code>, then you also must provide <code>MinimumProtocolVersion</code> and <code>SslSupportMethod</code>.</p>"""
    minimum_protocol_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The security policy that CloudFront uses for HTTPS connections with viewers. If <code>SslSupportMethod</code> is <code>sni-only</code>, then <code>MinimumProtocolVersion</code> must be <code>TLSv1</code> or higher.</p>"""
    ssl_support_method: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The viewers that the distribution accepts HTTPS connections from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionViewerCertificate) -> dict:
    out: dict = {}
    if "acm_certificate_arn" in value:
        out["AcmCertificateArn"] = value["acm_certificate_arn"]
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_source" in value:
        out["CertificateSource"] = value["certificate_source"]
    if "cloud_front_default_certificate" in value:
        out["CloudFrontDefaultCertificate"] = value["cloud_front_default_certificate"]
    if "iam_certificate_id" in value:
        out["IamCertificateId"] = value["iam_certificate_id"]
    if "minimum_protocol_version" in value:
        out["MinimumProtocolVersion"] = value["minimum_protocol_version"]
    if "ssl_support_method" in value:
        out["SslSupportMethod"] = value["ssl_support_method"]
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionViewerCertificate:
    out: AwsCloudFrontDistributionViewerCertificate = {}  # type: ignore[typeddict-item]
    if "AcmCertificateArn" in data:
        out["acm_certificate_arn"] = data["AcmCertificateArn"]
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    if "CertificateSource" in data:
        out["certificate_source"] = data["CertificateSource"]
    if "CloudFrontDefaultCertificate" in data:
        out["cloud_front_default_certificate"] = data["CloudFrontDefaultCertificate"]
    if "IamCertificateId" in data:
        out["iam_certificate_id"] = data["IamCertificateId"]
    if "MinimumProtocolVersion" in data:
        out["minimum_protocol_version"] = data["MinimumProtocolVersion"]
    if "SslSupportMethod" in data:
        out["ssl_support_method"] = data["SslSupportMethod"]
    return out
