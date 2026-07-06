"""Generated from Smithy shape ``com.amazonaws.iot#CreateDomainConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.acm_certificate_arn
    import aws_sdk_iot.types.application_protocol
    import aws_sdk_iot.types.authentication_type
    import aws_sdk_iot.types.authorizer_config
    import aws_sdk_iot.types.client_certificate_config
    import aws_sdk_iot.types.domain_configuration_name
    import aws_sdk_iot.types.domain_name
    import aws_sdk_iot.types.server_certificate_arns
    import aws_sdk_iot.types.server_certificate_config
    import aws_sdk_iot.types.service_type
    import aws_sdk_iot.types.tag_list
    import aws_sdk_iot.types.tls_config


class CreateDomainConfigurationRequest(TypedDict, closed=True):
    domain_configuration_name: (
        "aws_sdk_iot.types.domain_configuration_name.DomainConfigurationName"
    )
    """<p>The name of the domain configuration. This value must be unique to a region.</p>"""
    domain_name: NotRequired["aws_sdk_iot.types.domain_name.DomainName"]
    """<p>The name of the domain.</p>"""
    server_certificate_arns: NotRequired[
        "aws_sdk_iot.types.server_certificate_arns.ServerCertificateArns"
    ]
    """<p>The ARNs of the certificates that IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for Amazon Web Services-managed domains.</p>"""
    validation_certificate_arn: NotRequired[
        "aws_sdk_iot.types.acm_certificate_arn.AcmCertificateArn"
    ]
    """<p>The certificate used to validate the server certificate and prove domain name ownership. This certificate must be signed by a public certificate authority. This value is not required for Amazon Web Services-managed domains.</p>"""
    authorizer_config: NotRequired[
        "aws_sdk_iot.types.authorizer_config.AuthorizerConfig"
    ]
    """<p>An object that specifies the authorization service for a domain.</p>"""
    service_type: NotRequired["aws_sdk_iot.types.service_type.ServiceType"]
    """<p>The type of service delivered by the endpoint.</p> <note> <p>Amazon Web Services IoT Core currently supports only the <code>DATA</code> service type.</p> </note>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    r"""<p>Metadata which can be used to manage the domain configuration.</p> <note> <p>For URI Request parameters use format: ...key1=value1&key2=value2...</p> <p>For the CLI command-line parameter use format: &&tags \"key1=value1&key2=value2...\"</p> <p>For the cli-input-json file use format: \"tags\": \"key1=value1&key2=value2...\"</p> </note>"""
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
def serialize_json(value: CreateDomainConfigurationRequest) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "server_certificate_arns" in value:
        import aws_sdk_iot.types.server_certificate_arns

        out["serverCertificateArns"] = (
            aws_sdk_iot.types.server_certificate_arns.serialize_json(
                value["server_certificate_arns"]
            )
        )
    if "validation_certificate_arn" in value:
        out["validationCertificateArn"] = value["validation_certificate_arn"]
    if "authorizer_config" in value:
        import aws_sdk_iot.types.authorizer_config

        out["authorizerConfig"] = aws_sdk_iot.types.authorizer_config.serialize_json(
            value["authorizer_config"]
        )
    if "service_type" in value:
        import aws_sdk_iot.types.service_type

        out["serviceType"] = aws_sdk_iot.types.service_type.serialize_json(
            value["service_type"]
        )
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
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


def deserialize_json(data: dict) -> CreateDomainConfigurationRequest:
    out: CreateDomainConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "serverCertificateArns" in data:
        import aws_sdk_iot.types.server_certificate_arns

        out["server_certificate_arns"] = (
            aws_sdk_iot.types.server_certificate_arns.deserialize_json(
                data["serverCertificateArns"]
            )
        )
    if "validationCertificateArn" in data:
        out["validation_certificate_arn"] = data["validationCertificateArn"]
    if "authorizerConfig" in data:
        import aws_sdk_iot.types.authorizer_config

        out["authorizer_config"] = aws_sdk_iot.types.authorizer_config.deserialize_json(
            data["authorizerConfig"]
        )
    if "serviceType" in data:
        import aws_sdk_iot.types.service_type

        out["service_type"] = aws_sdk_iot.types.service_type.deserialize_json(
            data["serviceType"]
        )
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
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
