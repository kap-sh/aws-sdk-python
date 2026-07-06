"""Generated from Smithy shape ``com.amazonaws.apigateway#CreateDomainNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_api_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.endpoint_access_mode
    import aws_sdk_api_gateway.types.endpoint_configuration
    import aws_sdk_api_gateway.types.map_of_string_to_string
    import aws_sdk_api_gateway.types.mutual_tls_authentication_input
    import aws_sdk_api_gateway.types.routing_mode
    import aws_sdk_api_gateway.types.security_policy
    import aws_sdk_api_gateway.types.string


class CreateDomainNameRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_api_gateway.types.string.String"
    """<p>The name of the DomainName resource.</p>"""
    certificate_name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The user-friendly name of the certificate that will be used by edge-optimized endpoint or private endpoint for this domain name.</p>"""
    certificate_body: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>[Deprecated] The body of the server certificate that will be used by edge-optimized endpoint or private endpoint for this domain name provided by your certificate authority.</p>"""
    certificate_private_key: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>[Deprecated] Your edge-optimized endpoint's domain name certificate's private key.</p>"""
    certificate_chain: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>[Deprecated] The intermediate certificates and optionally the root certificate, one after the other without any blank lines, used by an edge-optimized endpoint for this domain name. If you include the root certificate, your certificate chain must start with intermediate certificates and end with the root certificate. Use the intermediate certificates that were provided by your certificate authority. Do not include any intermediaries that are not in the chain of trust path.</p>"""
    certificate_arn: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint or private endpoint for this domain name. Certificate Manager is the only supported source.</p>"""
    regional_certificate_name: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The user-friendly name of the certificate that will be used by regional endpoint for this domain name.</p>"""
    regional_certificate_arn: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>The reference to an Amazon Web Services-managed certificate that will be used by regional endpoint for this domain name. Certificate Manager is the only supported source.</p>"""
    endpoint_configuration: NotRequired[
        "aws_sdk_api_gateway.types.endpoint_configuration.EndpointConfiguration"
    ]
    """<p>The endpoint configuration of this DomainName showing the endpoint types and IP address types of the domain name. </p>"""
    tags: NotRequired[
        "aws_sdk_api_gateway.types.map_of_string_to_string.MapOfStringToString"
    ]
    """<p>The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with <code>aws:</code>. The tag value can be up to 256 characters.</p>"""
    security_policy: NotRequired[
        "aws_sdk_api_gateway.types.security_policy.SecurityPolicy"
    ]
    """<p>The Transport Layer Security (TLS) version + cipher suite for this DomainName.</p>"""
    endpoint_access_mode: NotRequired[
        "aws_sdk_api_gateway.types.endpoint_access_mode.EndpointAccessMode"
    ]
    """<p> The endpoint access mode of the DomainName. Only available for DomainNames that use security policies that start with <code>SecurityPolicy_</code>. </p>"""
    mutual_tls_authentication: NotRequired[
        "aws_sdk_api_gateway.types.mutual_tls_authentication_input.MutualTlsAuthenticationInput"
    ]
    ownership_verification_certificate_arn: NotRequired[
        "aws_sdk_api_gateway.types.string.String"
    ]
    """<p>The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn.</p>"""
    policy: NotRequired["aws_sdk_api_gateway.types.string.String"]
    """<p>A stringified JSON policy document that applies to the <code>execute-api</code> service for this DomainName regardless of the caller and Method configuration. Supported only for private custom domain names.</p>"""
    routing_mode: NotRequired["aws_sdk_api_gateway.types.routing_mode.RoutingMode"]
    """<p> The routing mode for this domain name. The routing mode determines how API Gateway sends traffic from your custom domain name to your private APIs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainNameRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "certificate_body" in value:
        out["certificateBody"] = value["certificate_body"]
    if "certificate_private_key" in value:
        out["certificatePrivateKey"] = value["certificate_private_key"]
    if "certificate_chain" in value:
        out["certificateChain"] = value["certificate_chain"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "regional_certificate_name" in value:
        out["regionalCertificateName"] = value["regional_certificate_name"]
    if "regional_certificate_arn" in value:
        out["regionalCertificateArn"] = value["regional_certificate_arn"]
    if "endpoint_configuration" in value:
        import aws_sdk_api_gateway.types.endpoint_configuration

        out["endpointConfiguration"] = (
            aws_sdk_api_gateway.types.endpoint_configuration.serialize_json(
                value["endpoint_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = aws_sdk_api_gateway.types.map_of_string_to_string.serialize_json(
            value["tags"]
        )
    if "security_policy" in value:
        import aws_sdk_api_gateway.types.security_policy

        out["securityPolicy"] = (
            aws_sdk_api_gateway.types.security_policy.serialize_json(
                value["security_policy"]
            )
        )
    if "endpoint_access_mode" in value:
        import aws_sdk_api_gateway.types.endpoint_access_mode

        out["endpointAccessMode"] = (
            aws_sdk_api_gateway.types.endpoint_access_mode.serialize_json(
                value["endpoint_access_mode"]
            )
        )
    if "mutual_tls_authentication" in value:
        import aws_sdk_api_gateway.types.mutual_tls_authentication_input

        out["mutualTlsAuthentication"] = (
            aws_sdk_api_gateway.types.mutual_tls_authentication_input.serialize_json(
                value["mutual_tls_authentication"]
            )
        )
    if "ownership_verification_certificate_arn" in value:
        out["ownershipVerificationCertificateArn"] = value[
            "ownership_verification_certificate_arn"
        ]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "routing_mode" in value:
        import aws_sdk_api_gateway.types.routing_mode

        out["routingMode"] = aws_sdk_api_gateway.types.routing_mode.serialize_json(
            value["routing_mode"]
        )
    return out


def deserialize_json(data: dict) -> CreateDomainNameRequest:
    out: CreateDomainNameRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("CreateDomainNameRequest.domain_name required")
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    if "certificateBody" in data:
        out["certificate_body"] = data["certificateBody"]
    if "certificatePrivateKey" in data:
        out["certificate_private_key"] = data["certificatePrivateKey"]
    if "certificateChain" in data:
        out["certificate_chain"] = data["certificateChain"]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "regionalCertificateName" in data:
        out["regional_certificate_name"] = data["regionalCertificateName"]
    if "regionalCertificateArn" in data:
        out["regional_certificate_arn"] = data["regionalCertificateArn"]
    if "endpointConfiguration" in data:
        import aws_sdk_api_gateway.types.endpoint_configuration

        out["endpoint_configuration"] = (
            aws_sdk_api_gateway.types.endpoint_configuration.deserialize_json(
                data["endpointConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_api_gateway.types.map_of_string_to_string

        out["tags"] = (
            aws_sdk_api_gateway.types.map_of_string_to_string.deserialize_json(
                data["tags"]
            )
        )
    if "securityPolicy" in data:
        import aws_sdk_api_gateway.types.security_policy

        out["security_policy"] = (
            aws_sdk_api_gateway.types.security_policy.deserialize_json(
                data["securityPolicy"]
            )
        )
    if "endpointAccessMode" in data:
        import aws_sdk_api_gateway.types.endpoint_access_mode

        out["endpoint_access_mode"] = (
            aws_sdk_api_gateway.types.endpoint_access_mode.deserialize_json(
                data["endpointAccessMode"]
            )
        )
    if "mutualTlsAuthentication" in data:
        import aws_sdk_api_gateway.types.mutual_tls_authentication_input

        out["mutual_tls_authentication"] = (
            aws_sdk_api_gateway.types.mutual_tls_authentication_input.deserialize_json(
                data["mutualTlsAuthentication"]
            )
        )
    if "ownershipVerificationCertificateArn" in data:
        out["ownership_verification_certificate_arn"] = data[
            "ownershipVerificationCertificateArn"
        ]
    if "policy" in data:
        out["policy"] = data["policy"]
    if "routingMode" in data:
        import aws_sdk_api_gateway.types.routing_mode

        out["routing_mode"] = aws_sdk_api_gateway.types.routing_mode.deserialize_json(
            data["routingMode"]
        )
    return out
