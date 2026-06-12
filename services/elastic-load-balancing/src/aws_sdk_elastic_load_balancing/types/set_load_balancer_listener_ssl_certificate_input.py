"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SetLoadBalancerListenerSSLCertificateInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.access_point_port
    import aws_sdk_elastic_load_balancing.types.ssl_certificate_id


class SetLoadBalancerListenerSSLCertificateInput(TypedDict):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    load_balancer_port: (
        "aws_sdk_elastic_load_balancing.types.access_point_port.AccessPointPort"
    )
    """<p>The port that uses the specified SSL certificate.</p>"""
    ssl_certificate_id: (
        "aws_sdk_elastic_load_balancing.types.ssl_certificate_id.SSLCertificateId"
    )
    """<p>The Amazon Resource Name (ARN) of the SSL certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetLoadBalancerListenerSSLCertificateInput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    pairs.append(
        (f"{prefix}.LoadBalancerPort", str(value.get("load_balancer_port", 0)))
    )
    pairs.append((f"{prefix}.SSLCertificateId", str(value["ssl_certificate_id"])))


def deserialize_query(el: Element) -> SetLoadBalancerListenerSSLCertificateInput:
    out: SetLoadBalancerListenerSSLCertificateInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "SetLoadBalancerListenerSSLCertificateInput.load_balancer_name required"
        )
    child_load_balancer_port = el.find("LoadBalancerPort")
    if child_load_balancer_port is not None:
        out["load_balancer_port"] = int(child_load_balancer_port.text or "")
    else:
        out["load_balancer_port"] = 0
    child_ssl_certificate_id = el.find("SSLCertificateId")
    if child_ssl_certificate_id is not None:
        out["ssl_certificate_id"] = str(child_ssl_certificate_id.text or "")
    else:
        raise DeserializationError(
            "SetLoadBalancerListenerSSLCertificateInput.ssl_certificate_id required"
        )
    return out
