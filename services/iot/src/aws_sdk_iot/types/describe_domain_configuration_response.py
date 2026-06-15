"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDomainConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.application_protocol
    import aws_sdk_iot.types.authentication_type
    import aws_sdk_iot.types.authorizer_config
    import aws_sdk_iot.types.client_certificate_config
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.domain_configuration_arn
    import aws_sdk_iot.types.domain_configuration_status
    import aws_sdk_iot.types.domain_name
    import aws_sdk_iot.types.domain_type
    import aws_sdk_iot.types.reserved_domain_configuration_name
    import aws_sdk_iot.types.server_certificate_config
    import aws_sdk_iot.types.server_certificates
    import aws_sdk_iot.types.service_type
    import aws_sdk_iot.types.tls_config


class DescribeDomainConfigurationResponse(TypedDict):
    domain_configuration_name: NotRequired[
        "aws_sdk_iot.types.reserved_domain_configuration_name.ReservedDomainConfigurationName"
    ]
    """<p>The name of the domain configuration.</p>"""
    domain_configuration_arn: NotRequired[
        "aws_sdk_iot.types.domain_configuration_arn.DomainConfigurationArn"
    ]
    """<p>The ARN of the domain configuration.</p>"""
    domain_name: NotRequired["aws_sdk_iot.types.domain_name.DomainName"]
    """<p>The name of the domain.</p>"""
    server_certificates: NotRequired[
        "aws_sdk_iot.types.server_certificates.ServerCertificates"
    ]
    """<p>A list containing summary information about the server certificate included in the domain configuration.</p>"""
    authorizer_config: NotRequired[
        "aws_sdk_iot.types.authorizer_config.AuthorizerConfig"
    ]
    """<p>An object that specifies the authorization service for a domain.</p>"""
    domain_configuration_status: NotRequired[
        "aws_sdk_iot.types.domain_configuration_status.DomainConfigurationStatus"
    ]
    """<p>A Boolean value that specifies the current state of the domain configuration.</p>"""
    service_type: NotRequired["aws_sdk_iot.types.service_type.ServiceType"]
    """<p>The type of service delivered by the endpoint.</p>"""
    domain_type: NotRequired["aws_sdk_iot.types.domain_type.DomainType"]
    """<p>The type of the domain.</p>"""
    last_status_change_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date and time the domain configuration's status was last changed.</p>"""
    tls_config: NotRequired["aws_sdk_iot.types.tls_config.TlsConfig"]
    """<p>An object that specifies the TLS configuration for a domain.</p>"""
    server_certificate_config: NotRequired[
        "aws_sdk_iot.types.server_certificate_config.ServerCertificateConfig"
    ]
    """<p>The server certificate configuration.</p>"""
    authentication_type: NotRequired[
        "aws_sdk_iot.types.authentication_type.AuthenticationType"
    ]
    r"""<p>An enumerated string that speciﬁes the authentication type.</p> <ul> <li> <p> <code>CUSTOM_AUTH_X509</code> - Use custom authentication and authorization with additional details from the X.509 client certificate.</p> </li> </ul> <ul> <li> <p> <code>CUSTOM_AUTH</code> - Use custom authentication and authorization. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html\">Custom authentication and authorization</a>.</p> </li> </ul> <ul> <li> <p> <code>AWS_X509</code> - Use X.509 client certificates without custom authentication and authorization. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html\">X.509 client certificates</a>.</p> </li> </ul> <ul> <li> <p> <code>AWS_SIGV4</code> - Use Amazon Web Services Signature Version 4. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html\">IAM users, groups, and roles</a>.</p> </li> </ul> <ul> <li> <p> <code>DEFAULT</code> - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify authentication type. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html\">Device communication protocols</a>.</p> </li> </ul>"""
    application_protocol: NotRequired[
        "aws_sdk_iot.types.application_protocol.ApplicationProtocol"
    ]
    r"""<p>An enumerated string that speciﬁes the application-layer protocol.</p> <ul> <li> <p> <code>SECURE_MQTT</code> - MQTT over TLS.</p> </li> </ul> <ul> <li> <p> <code>MQTT_WSS</code> - MQTT over WebSocket.</p> </li> </ul> <ul> <li> <p> <code>HTTPS</code> - HTTP over TLS.</p> </li> </ul> <ul> <li> <p> <code>DEFAULT</code> - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify application_layer protocol. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html\">Device communication protocols</a>.</p> </li> </ul>"""
    client_certificate_config: NotRequired[
        "aws_sdk_iot.types.client_certificate_config.ClientCertificateConfig"
    ]
    """<p>An object that speciﬁes the client certificate conﬁguration for a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainConfigurationResponse) -> dict:
    out: dict = {}
    if "domain_configuration_name" in value:
        out["domainConfigurationName"] = value["domain_configuration_name"]
    if "domain_configuration_arn" in value:
        out["domainConfigurationArn"] = value["domain_configuration_arn"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "server_certificates" in value:
        import aws_sdk_iot.types.server_certificates

        out["serverCertificates"] = (
            aws_sdk_iot.types.server_certificates.serialize_json(
                value["server_certificates"]
            )
        )
    if "authorizer_config" in value:
        import aws_sdk_iot.types.authorizer_config

        out["authorizerConfig"] = aws_sdk_iot.types.authorizer_config.serialize_json(
            value["authorizer_config"]
        )
    if "domain_configuration_status" in value:
        import aws_sdk_iot.types.domain_configuration_status

        out["domainConfigurationStatus"] = (
            aws_sdk_iot.types.domain_configuration_status.serialize_json(
                value["domain_configuration_status"]
            )
        )
    if "service_type" in value:
        import aws_sdk_iot.types.service_type

        out["serviceType"] = aws_sdk_iot.types.service_type.serialize_json(
            value["service_type"]
        )
    if "domain_type" in value:
        import aws_sdk_iot.types.domain_type

        out["domainType"] = aws_sdk_iot.types.domain_type.serialize_json(
            value["domain_type"]
        )
    if "last_status_change_date" in value:
        import aws_sdk_iot.types.date_type

        out["lastStatusChangeDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_status_change_date"]
        )
    if "tls_config" in value:
        import aws_sdk_iot.types.tls_config

        out["tlsConfig"] = aws_sdk_iot.types.tls_config.serialize_json(
            value["tls_config"]
        )
    if "server_certificate_config" in value:
        import aws_sdk_iot.types.server_certificate_config

        out["serverCertificateConfig"] = (
            aws_sdk_iot.types.server_certificate_config.serialize_json(
                value["server_certificate_config"]
            )
        )
    if "authentication_type" in value:
        import aws_sdk_iot.types.authentication_type

        out["authenticationType"] = (
            aws_sdk_iot.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "application_protocol" in value:
        import aws_sdk_iot.types.application_protocol

        out["applicationProtocol"] = (
            aws_sdk_iot.types.application_protocol.serialize_json(
                value["application_protocol"]
            )
        )
    if "client_certificate_config" in value:
        import aws_sdk_iot.types.client_certificate_config

        out["clientCertificateConfig"] = (
            aws_sdk_iot.types.client_certificate_config.serialize_json(
                value["client_certificate_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDomainConfigurationResponse:
    out: DescribeDomainConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "domainConfigurationName" in data:
        out["domain_configuration_name"] = data["domainConfigurationName"]
    if "domainConfigurationArn" in data:
        out["domain_configuration_arn"] = data["domainConfigurationArn"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "serverCertificates" in data:
        import aws_sdk_iot.types.server_certificates

        out["server_certificates"] = (
            aws_sdk_iot.types.server_certificates.deserialize_json(
                data["serverCertificates"]
            )
        )
    if "authorizerConfig" in data:
        import aws_sdk_iot.types.authorizer_config

        out["authorizer_config"] = aws_sdk_iot.types.authorizer_config.deserialize_json(
            data["authorizerConfig"]
        )
    if "domainConfigurationStatus" in data:
        import aws_sdk_iot.types.domain_configuration_status

        out["domain_configuration_status"] = (
            aws_sdk_iot.types.domain_configuration_status.deserialize_json(
                data["domainConfigurationStatus"]
            )
        )
    if "serviceType" in data:
        import aws_sdk_iot.types.service_type

        out["service_type"] = aws_sdk_iot.types.service_type.deserialize_json(
            data["serviceType"]
        )
    if "domainType" in data:
        import aws_sdk_iot.types.domain_type

        out["domain_type"] = aws_sdk_iot.types.domain_type.deserialize_json(
            data["domainType"]
        )
    if "lastStatusChangeDate" in data:
        import aws_sdk_iot.types.date_type

        out["last_status_change_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastStatusChangeDate"]
        )
    if "tlsConfig" in data:
        import aws_sdk_iot.types.tls_config

        out["tls_config"] = aws_sdk_iot.types.tls_config.deserialize_json(
            data["tlsConfig"]
        )
    if "serverCertificateConfig" in data:
        import aws_sdk_iot.types.server_certificate_config

        out["server_certificate_config"] = (
            aws_sdk_iot.types.server_certificate_config.deserialize_json(
                data["serverCertificateConfig"]
            )
        )
    if "authenticationType" in data:
        import aws_sdk_iot.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_iot.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    if "applicationProtocol" in data:
        import aws_sdk_iot.types.application_protocol

        out["application_protocol"] = (
            aws_sdk_iot.types.application_protocol.deserialize_json(
                data["applicationProtocol"]
            )
        )
    if "clientCertificateConfig" in data:
        import aws_sdk_iot.types.client_certificate_config

        out["client_certificate_config"] = (
            aws_sdk_iot.types.client_certificate_config.deserialize_json(
                data["clientCertificateConfig"]
            )
        )
    return out
