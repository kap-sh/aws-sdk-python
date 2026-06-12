"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Listener``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.actions
    import aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name
    import aws_sdk_elastic_load_balancing_v2.types.certificate_list
    import aws_sdk_elastic_load_balancing_v2.types.listener_arn
    import aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn
    import aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes
    import aws_sdk_elastic_load_balancing_v2.types.port
    import aws_sdk_elastic_load_balancing_v2.types.protocol_enum
    import aws_sdk_elastic_load_balancing_v2.types.ssl_policy_name


class Listener(TypedDict):
    listener_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    load_balancer_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    port: NotRequired["aws_sdk_elastic_load_balancing_v2.types.port.Port"]
    """<p>The port on which the load balancer is listening.</p>"""
    protocol: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.protocol_enum.ProtocolEnum"
    ]
    """<p>The protocol for connections from clients to the load balancer.</p>"""
    certificates: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.certificate_list.CertificateList"
    ]
    """<p>[HTTPS or TLS listener] The default certificate for the listener.</p>"""
    ssl_policy: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.ssl_policy_name.SslPolicyName"
    ]
    """<p>[HTTPS or TLS listener] The security policy that defines which protocols and ciphers are supported.</p>"""
    default_actions: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.actions.Actions"
    ]
    """<p>The default actions for the listener.</p>"""
    alpn_policy: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.alpn_policy_name.AlpnPolicyName"
    ]
    """<p>[TLS listener] The name of the Application-Layer Protocol Negotiation (ALPN) policy.</p>"""
    mutual_authentication: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.mutual_authentication_attributes.MutualAuthenticationAttributes"
    ]
    """<p>The mutual authentication configuration information.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Listener, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "listener_arn" in value:
        pairs.append((f"{prefix}.ListenerArn", str(value["listener_arn"])))
    if "load_balancer_arn" in value:
        pairs.append((f"{prefix}.LoadBalancerArn", str(value["load_balancer_arn"])))
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "protocol" in value:
        import aws_sdk_elastic_load_balancing_v2.types.protocol_enum

        aws_sdk_elastic_load_balancing_v2.types.protocol_enum.serialize_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "certificates" in value:
        import aws_sdk_elastic_load_balancing_v2.types.certificate_list

        aws_sdk_elastic_load_balancing_v2.types.certificate_list.serialize_query(
            value["certificates"], pairs, f"{prefix}.Certificates"
        )
    if "ssl_policy" in value:
        pairs.append((f"{prefix}.SslPolicy", str(value["ssl_policy"])))
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


def deserialize_query(el: Element) -> Listener:
    out: Listener = {}  # type: ignore[typeddict-item]
    child_listener_arn = el.find("ListenerArn")
    if child_listener_arn is not None:
        out["listener_arn"] = str(child_listener_arn.text or "")
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
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
    child_certificates = el.find("Certificates")
    if child_certificates is not None:
        import aws_sdk_elastic_load_balancing_v2.types.certificate_list

        out["certificates"] = (
            aws_sdk_elastic_load_balancing_v2.types.certificate_list.deserialize_query(
                child_certificates
            )
        )
    child_ssl_policy = el.find("SslPolicy")
    if child_ssl_policy is not None:
        out["ssl_policy"] = str(child_ssl_policy.text or "")
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
