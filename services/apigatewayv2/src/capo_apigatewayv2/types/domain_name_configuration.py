"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DomainNameConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.__timestamp_iso8601
    import capo_apigatewayv2.types.arn
    import capo_apigatewayv2.types.domain_name_status
    import capo_apigatewayv2.types.endpoint_type
    import capo_apigatewayv2.types.ip_address_type
    import capo_apigatewayv2.types.security_policy
    import capo_apigatewayv2.types.string_with_length_between1_and128


class DomainNameConfiguration(TypedDict, closed=True):
    api_gateway_domain_name: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>A domain name for the API.</p>"""
    certificate_arn: NotRequired["capo_apigatewayv2.types.arn.Arn"]
    """<p>An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.</p>"""
    certificate_name: NotRequired[
        "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
    ]
    """<p>The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.</p>"""
    certificate_upload_date: NotRequired[
        "capo_apigatewayv2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded.</p>"""
    domain_name_status: NotRequired[
        "capo_apigatewayv2.types.domain_name_status.DomainNameStatus"
    ]
    """<p>The status of the domain name migration. The valid values are AVAILABLE, UPDATING, PENDING_CERTIFICATE_REIMPORT, and PENDING_OWNERSHIP_VERIFICATION. If the status is UPDATING, the domain cannot be modified further until the existing operation is complete. If it is AVAILABLE, the domain can be updated.</p>"""
    domain_name_status_message: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>An optional text message containing detailed information about status of the domain name migration.</p>"""
    endpoint_type: NotRequired["capo_apigatewayv2.types.endpoint_type.EndpointType"]
    """<p>The endpoint type.</p>"""
    hosted_zone_id: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The Amazon Route 53 Hosted Zone ID of the endpoint.</p>"""
    ip_address_type: NotRequired[
        "capo_apigatewayv2.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address types that can invoke the domain name. Use ipv4 to allow only IPv4 addresses to invoke your domain name, or use dualstack to allow both IPv4 and IPv6 addresses to invoke your domain name.</p>"""
    security_policy: NotRequired[
        "capo_apigatewayv2.types.security_policy.SecurityPolicy"
    ]
    """<p>The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are TLS_1_0 and TLS_1_2.</p>"""
    ownership_verification_certificate_arn: NotRequired[
        "capo_apigatewayv2.types.arn.Arn"
    ]
    """<p>The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameConfiguration) -> dict:
    out: dict = {}
    if "api_gateway_domain_name" in value:
        out["apiGatewayDomainName"] = value["api_gateway_domain_name"]
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "certificate_upload_date" in value:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["certificateUploadDate"] = (
            capo_apigatewayv2.types.__timestamp_iso8601.serialize_json(
                value["certificate_upload_date"]
            )
        )
    if "domain_name_status" in value:
        import capo_apigatewayv2.types.domain_name_status

        out["domainNameStatus"] = (
            capo_apigatewayv2.types.domain_name_status.serialize_json(
                value["domain_name_status"]
            )
        )
    if "domain_name_status_message" in value:
        out["domainNameStatusMessage"] = value["domain_name_status_message"]
    if "endpoint_type" in value:
        import capo_apigatewayv2.types.endpoint_type

        out["endpointType"] = capo_apigatewayv2.types.endpoint_type.serialize_json(
            value["endpoint_type"]
        )
    if "hosted_zone_id" in value:
        out["hostedZoneId"] = value["hosted_zone_id"]
    if "ip_address_type" in value:
        import capo_apigatewayv2.types.ip_address_type

        out["ipAddressType"] = capo_apigatewayv2.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "security_policy" in value:
        import capo_apigatewayv2.types.security_policy

        out["securityPolicy"] = capo_apigatewayv2.types.security_policy.serialize_json(
            value["security_policy"]
        )
    if "ownership_verification_certificate_arn" in value:
        out["ownershipVerificationCertificateArn"] = value[
            "ownership_verification_certificate_arn"
        ]
    return out


def deserialize_json(data: dict) -> DomainNameConfiguration:
    out: DomainNameConfiguration = {}  # type: ignore[typeddict-item]
    if "apiGatewayDomainName" in data:
        out["api_gateway_domain_name"] = data["apiGatewayDomainName"]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateName" in data:
        out["certificate_name"] = data["certificateName"]
    if "certificateUploadDate" in data:
        import capo_apigatewayv2.types.__timestamp_iso8601

        out["certificate_upload_date"] = (
            capo_apigatewayv2.types.__timestamp_iso8601.deserialize_json(
                data["certificateUploadDate"]
            )
        )
    if "domainNameStatus" in data:
        import capo_apigatewayv2.types.domain_name_status

        out["domain_name_status"] = (
            capo_apigatewayv2.types.domain_name_status.deserialize_json(
                data["domainNameStatus"]
            )
        )
    if "domainNameStatusMessage" in data:
        out["domain_name_status_message"] = data["domainNameStatusMessage"]
    if "endpointType" in data:
        import capo_apigatewayv2.types.endpoint_type

        out["endpoint_type"] = capo_apigatewayv2.types.endpoint_type.deserialize_json(
            data["endpointType"]
        )
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    if "ipAddressType" in data:
        import capo_apigatewayv2.types.ip_address_type

        out["ip_address_type"] = (
            capo_apigatewayv2.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if "securityPolicy" in data:
        import capo_apigatewayv2.types.security_policy

        out["security_policy"] = (
            capo_apigatewayv2.types.security_policy.deserialize_json(
                data["securityPolicy"]
            )
        )
    if "ownershipVerificationCertificateArn" in data:
        out["ownership_verification_certificate_arn"] = data[
            "ownershipVerificationCertificateArn"
        ]
    return out
