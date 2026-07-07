"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainDomainEndpointOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsOpenSearchServiceDomainDomainEndpointOptionsDetails(TypedDict, closed=True):
    custom_endpoint_certificate_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN for the security certificate. The certificate is managed in ACM.</p>"""
    custom_endpoint_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to enable a custom endpoint for the domain.</p>"""
    enforce_https: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to require that all traffic to the domain arrive over HTTPS.</p>"""
    custom_endpoint: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The fully qualified URL for the custom endpoint.</p>"""
    tls_security_policy: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The TLS security policy to apply to the HTTPS endpoint of the OpenSearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsOpenSearchServiceDomainDomainEndpointOptionsDetails,
) -> dict:
    out: dict = {}
    if "custom_endpoint_certificate_arn" in value:
        out["CustomEndpointCertificateArn"] = value["custom_endpoint_certificate_arn"]
    if "custom_endpoint_enabled" in value:
        out["CustomEndpointEnabled"] = value["custom_endpoint_enabled"]
    if "enforce_https" in value:
        out["EnforceHTTPS"] = value["enforce_https"]
    if "custom_endpoint" in value:
        out["CustomEndpoint"] = value["custom_endpoint"]
    if "tls_security_policy" in value:
        out["TLSSecurityPolicy"] = value["tls_security_policy"]
    return out


def deserialize_json(
    data: dict,
) -> AwsOpenSearchServiceDomainDomainEndpointOptionsDetails:
    out: AwsOpenSearchServiceDomainDomainEndpointOptionsDetails = {}  # type: ignore[typeddict-item]
    if "CustomEndpointCertificateArn" in data:
        out["custom_endpoint_certificate_arn"] = data["CustomEndpointCertificateArn"]
    if "CustomEndpointEnabled" in data:
        out["custom_endpoint_enabled"] = data["CustomEndpointEnabled"]
    if "EnforceHTTPS" in data:
        out["enforce_https"] = data["EnforceHTTPS"]
    if "CustomEndpoint" in data:
        out["custom_endpoint"] = data["CustomEndpoint"]
    if "TLSSecurityPolicy" in data:
        out["tls_security_policy"] = data["TLSSecurityPolicy"]
    return out
