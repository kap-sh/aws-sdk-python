"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainEndpointOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.arn
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.domain_name_fqdn
    import aws_sdk_elasticsearch_service.types.tls_security_policy


class DomainEndpointOptions(TypedDict):
    enforce_https: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p>Specify if only HTTPS endpoint should be enabled for the Elasticsearch domain.</p>"""
    tls_security_policy: NotRequired[
        "aws_sdk_elasticsearch_service.types.tls_security_policy.TLSSecurityPolicy"
    ]
    """<p>Specify the TLS security policy that needs to be applied to the HTTPS endpoint of Elasticsearch domain. <br></br> It can be one of the following values: <ul> <li><b>Policy-Min-TLS-1-0-2019-07: </b> TLS security policy that supports TLS version 1.0 to TLS version 1.2</li> <li><b>Policy-Min-TLS-1-2-2019-07: </b> TLS security policy that supports only TLS version 1.2</li> <li><b>Policy-Min-TLS-1-2-PFS-2023-10: </b> TLS security policy that supports TLS version 1.2 to TLS version 1.3 with perfect forward secrecy cipher suites</li> <li><b>Policy-Min-TLS-1-2-RFC9151-FIPS-2024-08: </b> TLS security policy that supports TLS version 1.3 with FIPS</li> </ul> </p>"""
    custom_endpoint_enabled: NotRequired[
        "aws_sdk_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p>Specify if custom endpoint should be enabled for the Elasticsearch domain.</p>"""
    custom_endpoint: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_name_fqdn.DomainNameFqdn"
    ]
    """<p>Specify the fully qualified domain for your custom endpoint.</p>"""
    custom_endpoint_certificate_arn: NotRequired[
        "aws_sdk_elasticsearch_service.types.arn.ARN"
    ]
    """<p>Specify ACM certificate ARN for your custom endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainEndpointOptions) -> dict:
    out: dict = {}
    if "enforce_https" in value:
        out["EnforceHTTPS"] = value["enforce_https"]
    if "tls_security_policy" in value:
        import aws_sdk_elasticsearch_service.types.tls_security_policy

        out["TLSSecurityPolicy"] = (
            aws_sdk_elasticsearch_service.types.tls_security_policy.serialize_json(
                value["tls_security_policy"]
            )
        )
    if "custom_endpoint_enabled" in value:
        out["CustomEndpointEnabled"] = value["custom_endpoint_enabled"]
    if "custom_endpoint" in value:
        out["CustomEndpoint"] = value["custom_endpoint"]
    if "custom_endpoint_certificate_arn" in value:
        out["CustomEndpointCertificateArn"] = value["custom_endpoint_certificate_arn"]
    return out


def deserialize_json(data: dict) -> DomainEndpointOptions:
    out: DomainEndpointOptions = {}  # type: ignore[typeddict-item]
    if "EnforceHTTPS" in data:
        out["enforce_https"] = data["EnforceHTTPS"]
    if "TLSSecurityPolicy" in data:
        import aws_sdk_elasticsearch_service.types.tls_security_policy

        out["tls_security_policy"] = (
            aws_sdk_elasticsearch_service.types.tls_security_policy.deserialize_json(
                data["TLSSecurityPolicy"]
            )
        )
    if "CustomEndpointEnabled" in data:
        out["custom_endpoint_enabled"] = data["CustomEndpointEnabled"]
    if "CustomEndpoint" in data:
        out["custom_endpoint"] = data["CustomEndpoint"]
    if "CustomEndpointCertificateArn" in data:
        out["custom_endpoint_certificate_arn"] = data["CustomEndpointCertificateArn"]
    return out
