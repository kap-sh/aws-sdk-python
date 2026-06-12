"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDomainConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.application_protocol
    import aws_sdk_iot.types.authentication_type
    import aws_sdk_iot.types.authorizer_config
    import aws_sdk_iot.types.client_certificate_config
    import aws_sdk_iot.types.domain_configuration_status
    import aws_sdk_iot.types.remove_authorizer_config
    import aws_sdk_iot.types.reserved_domain_configuration_name
    import aws_sdk_iot.types.server_certificate_config
    import aws_sdk_iot.types.tls_config


class UpdateDomainConfigurationRequest(TypedDict):
    domain_configuration_name: "aws_sdk_iot.types.reserved_domain_configuration_name.ReservedDomainConfigurationName"
    """<p>The name of the domain configuration to be updated.</p>"""
    authorizer_config: NotRequired[
        "aws_sdk_iot.types.authorizer_config.AuthorizerConfig"
    ]
    """<p>An object that specifies the authorization service for a domain.</p>"""
    domain_configuration_status: NotRequired[
        "aws_sdk_iot.types.domain_configuration_status.DomainConfigurationStatus"
    ]
    """<p>The status to which the domain configuration should be updated.</p>"""
    remove_authorizer_config: (
        "aws_sdk_iot.types.remove_authorizer_config.RemoveAuthorizerConfig"
    )
    """<p>Removes the authorization configuration from a domain.</p>"""
    tls_config: NotRequired["aws_sdk_iot.types.tls_config.TlsConfig"]
    """<p>An object that specifies the TLS configuration for a domain.</p>"""
    server_certificate_config: NotRequired[
        "aws_sdk_iot.types.server_certificate_config.ServerCertificateConfig"
    ]
    """<p>The server certificate configuration.</p>"""
    authentication_type: NotRequired[
        "aws_sdk_iot.types.authentication_type.AuthenticationType"
    ]
    """<p>An enumerated string that speciﬁes the authentication type.</p> <ul> <li> <p> <code>CUSTOM_AUTH_X509</code> - Use custom authentication and authorization with additional details from the X.509 client certificate.</p> </li> </ul> <ul> <li> <p> <code>CUSTOM_AUTH</code> - Use custom authentication and authorization. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html\">Custom authentication and authorization</a>.</p> </li> </ul> <ul> <li> <p> <code>AWS_X509</code> - Use X.509 client certificates without custom authentication and authorization. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html\">X.509 client certificates</a>.</p> </li> </ul> <ul> <li> <p> <code>AWS_SIGV4</code> - Use Amazon Web Services Signature Version 4. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html\">IAM users, groups, and roles</a>.</p> </li> </ul> <ul> <li> <p> <code>DEFAULT </code> - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify authentication type. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html\">Device communication protocols</a>.</p> </li> </ul>"""
    application_protocol: NotRequired[
        "aws_sdk_iot.types.application_protocol.ApplicationProtocol"
    ]
    """<p>An enumerated string that speciﬁes the application-layer protocol.</p> <ul> <li> <p> <code>SECURE_MQTT</code> - MQTT over TLS.</p> </li> </ul> <ul> <li> <p> <code>MQTT_WSS</code> - MQTT over WebSocket.</p> </li> </ul> <ul> <li> <p> <code>HTTPS</code> - HTTP over TLS.</p> </li> </ul> <ul> <li> <p> <code>DEFAULT</code> - Use a combination of port and Application Layer Protocol Negotiation (ALPN) to specify application_layer protocol. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html\">Device communication protocols</a>.</p> </li> </ul>"""
    client_certificate_config: NotRequired[
        "aws_sdk_iot.types.client_certificate_config.ClientCertificateConfig"
    ]
    """<p>An object that speciﬁes the client certificate conﬁguration for a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainConfigurationRequest) -> dict:
    out: dict = {}
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
    out["removeAuthorizerConfig"] = value.get("remove_authorizer_config", False)
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


def deserialize_json(data: dict) -> UpdateDomainConfigurationRequest:
    out: UpdateDomainConfigurationRequest = {}  # type: ignore[typeddict-item]
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
    if "removeAuthorizerConfig" in data:
        out["remove_authorizer_config"] = data["removeAuthorizerConfig"]
    else:
        out["remove_authorizer_config"] = False
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
