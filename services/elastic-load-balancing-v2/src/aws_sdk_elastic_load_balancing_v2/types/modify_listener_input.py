"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyListenerInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.actions
    import aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name
    import aws_sdk_elastic_load_balancing_v2.types.certificate_list
    import aws_sdk_elastic_load_balancing_v2.types.listener_arn
    import aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes
    import aws_sdk_elastic_load_balancing_v2.types.port
    import aws_sdk_elastic_load_balancing_v2.types.protocol_enum
    import aws_sdk_elastic_load_balancing_v2.types.ssl_policy_name


class ModifyListenerInput(TypedDict):
    listener_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    port: NotRequired["aws_sdk_elastic_load_balancing_v2.types.port.Port"]
    """<p>The port for connections from clients to the load balancer. You can't specify a port for a Gateway Load Balancer.</p>"""
    protocol: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
    ]
    """<p>The protocol for connections from clients to the load balancer. Application Load Balancers support the HTTP and HTTPS protocols. Network Load Balancers support the TCP, TLS, UDP, TCP_UDP, QUIC, and TCP_QUIC protocols. You can’t change the protocol to UDP, TCP_UDP, QUIC, or TCP_QUIC if dual-stack mode is enabled. You can't specify a protocol for a Gateway Load Balancer.</p>"""
    ssl_policy: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.ssl_policy_name.SslPolicyName"
    ]
    r"""<p>[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html\">Security policies</a> in the <i>Application Load Balancers Guide</i> or <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html\">Security policies</a> in the <i>Network Load Balancers Guide</i>.</p>"""
    certificates: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.certificate_list.CertificateList"
    ]
    """<p>[HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set <code>CertificateArn</code> to the certificate ARN but do not set <code>IsDefault</code>.</p>"""
    default_actions: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.actions.Actions"
    ]
    """<p>The actions for the default rule.</p>"""
    alpn_policy: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name.AlpnPolicyName"
    ]
    r"""<p>[TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:</p> <ul> <li> <p> <code>HTTP1Only</code> </p> </li> <li> <p> <code>HTTP2Only</code> </p> </li> <li> <p> <code>HTTP2Optional</code> </p> </li> <li> <p> <code>HTTP2Preferred</code> </p> </li> <li> <p> <code>None</code> </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html#alpn-policies\">ALPN policies</a> in the <i>Network Load Balancers Guide</i>.</p>"""
    mutual_authentication: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes.MutualAuthenticationAttributes"
    ]
    """<p>[HTTPS listeners] The mutual authentication configuration information.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyListenerInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "listener_arn" in value:
        pairs.append((f"{prefix}.ListenerArn", str(value["listener_arn"])))
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "protocol" in value:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        aws_sdk_elastic_load_balancing_v2.types.protocol_enum.serialize_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "ssl_policy" in value:
        pairs.append((f"{prefix}.SslPolicy", str(value["ssl_policy"])))
    if "certificates" in value:
        import aws_sdk_elastic_load_balancing_v2.types.certificate_list

        aws_sdk_elastic_load_balancing_v2.types.certificate_list.serialize_query(
            value["certificates"], pairs, f"{prefix}.Certificates"
        )
    if "default_actions" in value:
        import aws_sdk_elastic_load_balancing_v2.types.actions

        aws_sdk_elastic_load_balancing_v2.types.actions.serialize_query(
            value["default_actions"], pairs, f"{prefix}.DefaultActions"
        )
    if "alpn_policy" in value:
        import aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name

        aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name.serialize_query(
            value["alpn_policy"], pairs, f"{prefix}.AlpnPolicy"
        )
    if "mutual_authentication" in value:
        import aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes

        aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes.serialize_query(
            value["mutual_authentication"], pairs, f"{prefix}.MutualAuthentication"
        )


def deserialize_query(el: Element) -> ModifyListenerInput:
    out: ModifyListenerInput = {}  # type: ignore[typeddict-item]
    child_listener_arn = el.find("ListenerArn")
    if child_listener_arn is not None:
        out["listener_arn"] = str(child_listener_arn.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        out["protocol"] = (
            aws_sdk_elastic_load_balancing_v2.types.protocol_enum.deserialize_query(
                child_protocol
            )
        )
    child_ssl_policy = el.find("SslPolicy")
    if child_ssl_policy is not None:
        out["ssl_policy"] = str(child_ssl_policy.text or "")
    child_certificates = el.find("Certificates")
    if child_certificates is not None:
        import aws_sdk_elastic_load_balancing_v2.types.certificate_list

        out["certificates"] = (
            aws_sdk_elastic_load_balancing_v2.types.certificate_list.deserialize_query(
                child_certificates
            )
        )
    child_default_actions = el.find("DefaultActions")
    if child_default_actions is not None:
        import aws_sdk_elastic_load_balancing_v2.types.actions

        out["default_actions"] = (
            aws_sdk_elastic_load_balancing_v2.types.actions.deserialize_query(
                child_default_actions
            )
        )
    child_alpn_policy = el.find("AlpnPolicy")
    if child_alpn_policy is not None:
        import aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name

        out["alpn_policy"] = (
            aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name.deserialize_query(
                child_alpn_policy
            )
        )
    child_mutual_authentication = el.find("MutualAuthentication")
    if child_mutual_authentication is not None:
        import aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes

        out["mutual_authentication"] = (
            aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes.deserialize_query(
                child_mutual_authentication
            )
        )
    return out
